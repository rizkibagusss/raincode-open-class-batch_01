# Level 7 — Final Challenge: Expense Tracker CLI

Kali ini kita sengaja tidak menggunakan Flask. Fokus Pertemuan 03 adalah data,
CRUD, SQL, dan komunikasi Python–MySQL. Terminal dipilih agar alur logikanya
terlihat tanpa menambah layer baru.

Jangan membuat aplikasi dari nol. Lengkapi `expense_tracker_cli.py` bertahap.
Jalankan dan uji setelah setiap step.

## Step 1 — Connection

Pastikan `get_connection()` berhasil dan `.env` sudah benar.

## Step 2 — Read

Lengkapi `lihat_transaksi()`:

- jalankan SELECT;
- ambil `fetchall()`;
- tampilkan empty state atau loop data.

## Step 3 — Create

Lengkapi `tambah_transaksi()`:

- ambil input nama dan total;
- jalankan INSERT berparameter;
- commit;
- tampilkan ID baru.

## Step 4 — Update

Lengkapi `edit_transaksi()` menggunakan ID dan `rowcount`.

## Step 5 — Delete

Lengkapi `hapus_transaksi()` dengan WHERE ID dan konfirmasi sederhana.

## Step 6 — Menu

Hubungkan pilihan 1–5 ke function yang tepat.

## Expected menu

```text
=== RAINCODE EXPENSE TRACKER ===
1. Lihat transaksi
2. Tambah transaksi
3. Edit transaksi
4. Hapus transaksi
5. Keluar
```

## Hint

1. Selesaikan satu function, uji, baru pindah ke function berikutnya.
2. Query mutation membutuhkan `db.commit()`.
3. Gunakan pola `try/finally` agar cursor dan connection tetap ditutup.

## Definition of done

- [ ] Data masih ada setelah CLI ditutup dan dibuka kembali.
- [ ] Value user dikirim sebagai params, bukan dirangkai ke query.
- [ ] UPDATE dan DELETE menargetkan ID.
- [ ] ID tidak ditemukan menghasilkan pesan yang jelas.
- [ ] Pilihan menu tidak valid tidak menghentikan program.
- [ ] Kamu bisa menjelaskan perjalanan data sampai MySQL.
