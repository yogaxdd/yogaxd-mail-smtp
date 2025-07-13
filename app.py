import imaplib
import email
from flask import Flask, render_template, request
import json
from email.header import decode_header

app = Flask(__name__)

# Load email config
with open('email_config.json') as f:
    EMAIL_ACCOUNTS = json.load(f)


def decode_mime_words(s):
    if not s:
        return ""
    decoded = decode_header(s)
    return ''.join(
        str(t[0], t[1] or 'utf-8') if isinstance(t[0], bytes) else t[0]
        for t in decoded
    )


def fetch_emails(account):
    try:
        mail = imaplib.IMAP4_SSL(account['imap_server'], account['imap_port'])
        mail.login(account['username'], account['password'])
        mail.select('inbox')

        result, data = mail.search(None, 'ALL')
        ids = data[0].split()[-20:][::-1]  # Get last 20 emails
        emails = []

        for i in ids:
            res, msg_data = mail.fetch(i, '(RFC822)')
            if res != 'OK':
                continue
            msg = email.message_from_bytes(msg_data[0][1])
            subject = decode_mime_words(msg.get('Subject'))
            from_ = decode_mime_words(msg.get('From'))
            date_ = msg.get('Date')

            body = ""
            if msg.is_multipart():
                # Cari text/plain dulu
                for part in msg.walk():
                    ctype = part.get_content_type()
                    if ctype == 'text/plain' and part.get_content_disposition() is None:
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                        break
                # Jika text/plain tidak ada, cari text/html
                if not body:
                    for part in msg.walk():
                        ctype = part.get_content_type()
                        if ctype == 'text/html' and part.get_content_disposition() is None:
                            body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                            break
            else:
                # Non-multipart: bisa text/plain atau text/html
                ctype = msg.get_content_type()
                if ctype == 'text/plain' or ctype == 'text/html':
                    body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

            emails.append({"subject": subject, "from": from_, "date": date_, "body": body})

        mail.logout()
        return emails

    except Exception as e:
        print("Error fetching emails:", e)
        return []


@app.route('/')
def index():
    return render_template('index.html', accounts=EMAIL_ACCOUNTS)


@app.route('/inbox')
def inbox():
    email_id = request.args.get('email')
    account = next((acc for acc in EMAIL_ACCOUNTS if acc['email'] == email_id), None)
    if not account:
        return "Account not found", 404
    emails = fetch_emails(account)
    return render_template('inbox.html', emails=emails, email_id=email_id)


if __name__ == "__main__":
    app.run(debug=True)
