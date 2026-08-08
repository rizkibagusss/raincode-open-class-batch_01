# 08 — Understanding Check dan Mini Challenge

Bagian penutup ini mendampingi halaman 52–55 modul.

## Understanding check

Jawab tanpa melihat catatan terlebih dahulu:

1. Mengapa data pada demo pertama hilang setelah refresh?
2. Apa perbedaan database, table, column, dan row?
3. Apa pasangan SQL untuk setiap huruf CRUD?
4. Mengapa Python membutuhkan connector untuk berbicara dengan MySQL?
5. Apa perbedaan tugas route, service, dan `database.py`?
6. Mengapa `UPDATE` dan `DELETE` perlu `WHERE`?
7. Ceritakan perjalanan `Kopi Susu — 25000` dari form sampai table.

## Challenge bertingkat

Kerjakan dari level yang sesuai; tidak wajib menyelesaikan semuanya saat live.

### Level 1 — Tambah transaksi

Gunakan form untuk menambah `Kopi Susu` dengan total `25000`, lalu buktikan data
masih ada setelah refresh.

### Level 2 — Tambah kategori

Tambahkan field `kategori` pada form, payload, validation, table MySQL, query,
response, dan table HTML. Tuliskan migration SQL-nya lebih dahulu.

### Level 3 — Edit nominal

Ubah total transaksi dengan PATCH. Pastikan hanya row dengan ID target yang
berubah.

### Level 4 — Filter kategori

Tambahkan filter kategori. Gunakan query berparameter dan tampilkan state kosong
jika tidak ada hasil.

### Bonus — Hitung total

Tampilkan jumlah seluruh nominal memakai:

```sql
SELECT SUM(total) AS grand_total FROM transactions;
```

## Definition of done

- Input valid tersimpan di MySQL.
- Input salah mendapat pesan yang dapat dipahami.
- Data tetap ada setelah refresh.
- Query menggunakan parameter untuk value user.
- UPDATE/DELETE menargetkan ID yang benar.
- Peserta dapat menjelaskan alurnya, bukan hanya menunjukkan hasil.

