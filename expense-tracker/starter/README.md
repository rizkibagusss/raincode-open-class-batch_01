# RainCode Expense Tracker — Starter

Ini bukan latihan folder-per-folder seperti `exercises/meet-03`.
Ini adalah versi sederhana yang langsung dapat dijalankan. Tujuannya agar kamu
dapat melihat hubungan antara API, aturan bisnis, dan query SQL tanpa harus
melewati Repository Pattern terlebih dahulu.

Anggap ini ujian akhir informal: kalau kamu bisa menyelesaikan ini
Alurnya dibuat pendek dan eksplisit:

```text
Route (app.py) -> Service + Query SQL -> db.execute() -> MySQL
```

## Apa yang Sudah Disiapkan

| Bagian | Status |
|---|---|
| `templates/*.html` | Sudah lengkap — tampilan, form, tabel |
| `static/css`, `static/js` | Sudah lengkap — styling & interaksi UI |
| `config.py`, `utils/logger.py` | Konfigurasi dan logging |
| `models/expense_model.py` | Bentuk data dan daftar kategori |
| `database/db.py` | Object `db` dengan satu method utama `db.execute()` |
| `services/expense_service.py` | Business logic dan query SQL per use case/API |
| `app.py` | Route Flask: dashboard, list, create, edit, delete, summary |

Repository sengaja belum digunakan pada versi ini. Setelah memahami hubungan
Route, Service, query, dan Database, buka versi `../final` untuk melihat query
dipindahkan ke Repository Layer.

## Cara Membaca Kode

Ikuti satu fitur dari URL sampai query:

1. Cari route, misalnya `POST /create`, di `app.py`.
2. Lihat method Service yang dipanggil: `create_expense(form_data)`.
3. Buka method tersebut di `services/expense_service.py`.
4. Query `INSERT` berada tepat di dalam method itu.
5. Query dijalankan melalui `db.execute(query, params)`.
6. Buka `database/db.py` untuk melihat commit, rollback, dan cleanup koneksi.

Contoh pola yang digunakan:

```python
query = "SELECT * FROM expenses WHERE id = %s"
expense = db.execute(query, (expense_id,), fetch="one")
```

Gunakan `fetch="one"` untuk satu row, `fetch="all"` untuk banyak row, dan tanpa
`fetch` untuk `INSERT`, `UPDATE`, atau `DELETE`.

## Cara Menjalankan

Pastikan MySQL Server berjalan. Buat database dan user terlebih dahulu:

```sql
CREATE DATABASE expense_tracker
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'expense_app'@'localhost' IDENTIFIED BY 'change-this-local-password';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX
    ON expense_tracker.* TO 'expense_app'@'localhost';
```

```bash
cd projects/expense-tracker/starter
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Buka `http://localhost:5000`. Aplikasi akan langsung berjalan jika kredensial
MySQL pada `.env` benar.

## Latihan yang Disarankan

1. Ubah query list agar hanya mengambil kategori tertentu.
2. Tambahkan filter tanggal dengan parameterized query.
3. Tambahkan satu kategori pada Model dan coba membuat expense.
4. Buat query total pengeluaran per bulan.
5. Bandingkan Service ini dengan Repository pada versi `../final`.

## Checklist

- [ ] Bisa menjelaskan mengapa value SQL memakai placeholder `%s`.
- [ ] Bisa menjelaskan perbedaan `fetch="one"`, `fetch="all"`, dan mutation.
- [ ] Bisa menunjukkan query yang dipanggil oleh setiap route.
- [ ] Bisa menjelaskan kapan commit dan rollback dijalankan.
- [ ] Sudah mencoba tambah, cari, edit, dan hapus expense lewat browser.

## Hasil Akhir

Setelah versi sederhana ini dipahami, lanjut ke `../final` untuk mempelajari
alur **Route → Service → Repository → Database** dan alasan query dipisahkan dari
business logic pada aplikasi yang lebih besar.

RainCode Open Class · Understand before memorizing.
