# YogaxD Email Viewer

Aplikasi web sederhana berbasis Flask untuk melihat inbox Gmail. Aplikasi ini memungkinkan Anda menghubungkan beberapa akun Gmail dan melihat email mereka melalui antarmuka web yang bersih.

## Fitur

- 📧 Dukungan multi-akun Gmail
- 🎨 Antarmuka web modern dan responsif
- 🌓 Toggle mode gelap/terang
- 📱 Desain ramah perangkat mobile
- 🔄 Refresh email real-time
- 📄 Penampil konten email dengan popup modal

## Persyaratan

- Python 3.7 atau lebih tinggi
- Akun Gmail dengan App Password yang diaktifkan
- Koneksi internet

## Instalasi

1. **Clone atau download repository ini**
   ```bash
   git clone <repository-url>
   cd YogaxD-Smtp
   ```

2. **Install dependensi yang diperlukan**
   ```bash
   pip install flask
   ```

3. **Konfigurasi akun email Anda**
   - Edit `email_config.json` dengan detail akun Gmail Anda
   - Lihat bagian [Tutorial App Password](#tutorial-app-password) di bawah

4. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

5. **Akses aplikasi**
   - Buka browser web Anda
   - Navigasi ke `http://localhost:5000`

## Konfigurasi

Aplikasi menggunakan `email_config.json` untuk menyimpan konfigurasi akun email. Setiap akun harus memiliki struktur berikut:

```json
{
  "email": "email-anda@gmail.com",
  "imap_server": "imap.gmail.com",
  "imap_port": 993,
  "username": "email-anda@gmail.com",
  "password": "app-password-anda"
}
```

## Tutorial App Password

### Mengapa App Password?

Gmail memerlukan App Password untuk aplikasi yang tidak menggunakan OAuth 2.0. Ini adalah fitur keamanan untuk melindungi akun Anda.

### Panduan Langkah demi Langkah untuk Mendapatkan App Password Gmail

#### Langkah 1: Aktifkan Autentikasi 2-Faktor
1. Kunjungi [Pengaturan Akun Google](https://myaccount.google.com/)
2. Klik "Keamanan" di sidebar kiri
3. Di bawah "Masuk ke Google," klik "Verifikasi 2 Langkah"
4. Ikuti petunjuk untuk mengaktifkan autentikasi 2-faktor

#### Langkah 2: Generate App Password
1. Kunjungi [Pengaturan Akun Google](https://myaccount.google.com/)
2. Klik "Keamanan" di sidebar kiri
3. Di bawah "Masuk ke Google," klik "Sandi aplikasi"
4. Anda mungkin perlu masuk lagi
5. Di bawah "Pilih aplikasi," pilih "Mail"
6. Di bawah "Pilih perangkat," pilih "Lainnya (Nama kustom)"
7. Masukkan nama seperti "YogaxD Email Viewer"
8. Klik "Generate"
9. Google akan menampilkan app password 16 karakter (contoh: "abcd efgh ijkl mnop")

#### Langkah 3: Gunakan App Password
1. Salin app password yang dihasilkan
2. Buka `email_config.json`
3. Ganti field `password` dengan app password Anda
4. Simpan file

### Contoh Konfigurasi

```json
[
  {
    "email": "email-anda@gmail.com",
    "imap_server": "imap.gmail.com",
    "imap_port": 993,
    "username": "email-anda@gmail.com",
    "password": "abcd efgh ijkl mnop"
  }
]
```

### Catatan Keamanan Penting

- ⚠️ **Jangan pernah bagikan app password Anda**
- ⚠️ **Jangan commit app password ke version control**
- ⚠️ **Gunakan app password berbeda untuk aplikasi berbeda**
- ⚠️ **Cabut app password yang tidak lagi Anda butuhkan**

## Cara Penggunaan

1. **Pilih Akun Email**
   - Di halaman utama, klik pada alamat email mana saja dari daftar
   - Ini akan membuka inbox untuk akun tersebut

2. **Lihat Email**
   - Inbox menampilkan 20 email terakhir
   - Klik pada email mana saja untuk melihat konten lengkapnya
   - Gunakan popup modal untuk membaca detail email

3. **Refresh Inbox**
   - Klik tombol "🔄 Refresh" untuk mengambil email terbaru

4. **Toggle Tema**
   - Klik "🌓 Dark Mode" untuk beralih antara tema terang dan gelap

## Struktur File

```
YogaxD-Smtp/
├── app.py                 # Aplikasi Flask utama
├── email_config.json      # Konfigurasi akun email
├── templates/
│   ├── index.html        # Template halaman utama
│   └── inbox.html        # Template halaman inbox
└── README.md             # File ini
```

## Troubleshooting

### Masalah Umum

1. **Error "Login failed"**
   - Verifikasi app password Anda benar
   - Pastikan autentikasi 2-faktor diaktifkan
   - Periksa bahwa alamat email cocok dengan username

2. **Error "Connection refused"**
   - Periksa koneksi internet Anda
   - Verifikasi IMAP diaktifkan di pengaturan Gmail
   - Pastikan server IMAP dan port benar

3. **Tidak ada email yang muncul**
   - Periksa apakah akun email memiliki email di inbox
   - Verifikasi akun memiliki izin yang tepat
   - Coba refresh halaman

### Pengaturan Gmail yang Perlu Diperiksa

1. **Aktifkan IMAP**
   - Buka Pengaturan Gmail → Forwarding and POP/IMAP
   - Aktifkan akses IMAP

2. **Izinkan aplikasi kurang aman** (jika diperlukan)
   - Catatan: App password lebih disukai daripada opsi ini

## Pertimbangan Keamanan

- Aplikasi ini menyimpan password email dalam bentuk plain text
- Pertimbangkan menggunakan environment variables untuk penggunaan produksi
- Secara teratur ganti app password Anda
- Pantau akun Gmail Anda untuk aktivitas mencurigakan

## Next Update
- Fix Bug (isi email kosong).

## Kontribusi

Jangan ragu untuk mengirimkan masalah dan permintaan peningkatan!

## Lisensi

Proyek ini untuk tujuan pendidikan. Gunakan dengan bertanggung jawab dan sesuai dengan ketentuan layanan Gmail.

---

**Catatan**: Aplikasi ini dirancang untuk penggunaan pribadi dan tujuan pendidikan. Selalu ikuti ketentuan layanan Gmail dan praktik keamanan terbaik. 