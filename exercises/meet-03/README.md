# Pertemuan 03 — Data, MySQL, dan CRUD

Di Pertemuan 01 kamu belajar mengolah data dengan Python. Di Pertemuan 02 kamu membuat form dan menampilkan data di browser. Sekarang kita akan menjawab satu pertanyaan baru: **bagaimana membuat data tetap ada setelah program berhenti?**

Benang merah latihan ini adalah **RainCode Expense Tracker** dengan data:

- Kopi Susu — Rp25.000
- Makan Siang — Rp35.000
- Transport — Rp15.000

Kali ini kita sengaja tidak menggunakan Flask. Fokus exercise adalah memahami data, memory, SQL, CRUD, dan bagaimana Python berkomunikasi dengan MySQL.
Interface terminal membantu kita melihat logikanya tanpa menambah layer baru.

## Urutan pengerjaan

| Urutan | Folder | Fokus |
|---:|---|---|
| 0 | [00-warm-up](00-warm-up) | Tebak output dan recall Python |
| 1 | [01-representasi-data](01-representasi-data) | Variable → dictionary → list |
| 2 | [02-memory-crud](02-memory-crud) | CREATE, READ, UPDATE, DELETE di memory |
| 3 | [03-memory-vs-persistent](03-memory-vs-persistent) | Mengapa kita membutuhkan database |
| 4 | [04-mysql-sql](04-mysql-sql) | Setup MySQL dan SQL CRUD langsung |
| 5 | [05-python-mysql](05-python-mysql) | Connection, cursor, fetch, commit |
| 6 | [06-debugging](06-debugging) | Lima bug data dan MySQL |
| 7 | [07-final-challenge](07-final-challenge) | Expense Tracker CLI bertahap |
| 8 | [08-bonus](08-bonus) | Kategori dan total pengeluaran |
| — | [answers](answers) | Pembanding setelah mencoba sendiri |

Gunakan alur belajar berikut pada setiap file:

```text
LIHAT → TEBAK → JALANKAN → UBAH → AMATI → JELASKAN
```

## Setup Python

Pastikan Python tersedia:

```powershell
python --version
```

Buat virtual environment dari folder `meet-03`:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Salin konfigurasi database:

```powershell
Copy-Item .env.example .env
```

Isi `DB_PASSWORD` sesuai MySQL lokalmu. Jangan memasukkan `.env` atau password
asli ke Git.

## Setup MySQL

Tool utama yang disarankan adalah **MySQL Workbench**, sama seperti live class.
Alternatifnya, query yang sama dapat dijalankan lewat terminal MySQL.

1. Pastikan MySQL Server berjalan.
2. Buka `04-mysql-sql/setup.sql` di MySQL Workbench.
3. Jalankan seluruh isi file.
4. Pastikan schema `raincode_expense` dan table `transactions` muncul.
5. Lanjutkan ke `04-mysql-sql/exercise.sql`.

Melalui terminal:

```powershell
mysql -u root -p < 04-mysql-sql/setup.sql
```

## Jika connection gagal

Periksa satu per satu:

- MySQL Server sudah berjalan;
- `DB_HOST` dan `DB_PORT` benar;
- `DB_USER` dan `DB_PASSWORD` benar;
- database `raincode_expense` sudah dibuat;
- user memiliki permission untuk database tersebut;
- file `.env` berada di folder `meet-03`.

Jangan mengubah banyak bagian sekaligus. Baca pesan error, periksa satu penyebab,
lalu jalankan kembali.

## Aturan latihan

- Tulis prediksi sebelum menekan Run.
- Kerjakan TODO dari atas ke bawah.
- Maksimal gunakan tiga hint sebelum membuka jawaban.
- Jalankan SELECT untuk membuktikan hasil INSERT, UPDATE, atau DELETE.
- UPDATE dan DELETE harus menargetkan row dengan `WHERE`.
- Buka `answers/` setelah mencoba sendiri minimal 15–20 menit.

## Target akhir

- [ ] Bisa membuat dan memanipulasi list of dictionaries.
- [ ] Bisa menjelaskan CRUD di memory.
- [ ] Bisa menjalankan CRUD SQL langsung di MySQL.
- [ ] Bisa membaca hasil MySQL sebagai list of dictionaries Python.
- [ ] Memahami connection, cursor, fetch, parameter, dan commit.
- [ ] Bisa menelusuri bug sederhana berdasarkan gejalanya.
- [ ] Bisa menyelesaikan Expense Tracker CLI tanpa Flask.

RainCode Open Class · Understand before memorizing.
