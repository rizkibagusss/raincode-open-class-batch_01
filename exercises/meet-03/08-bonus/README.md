# Level Bonus — Eksperimen Mandiri

Kerjakan setelah CRUD utama dan CLI selesai.

## 🌱 BASIC

Pastikan seluruh CRUD transaksi bekerja dan data bertahan setelah program ditutup.

## 🌿 GROW — Tambah kategori

Tambahkan `kategori` pada seluruh perjalanan data:

1. Buat perubahan column database terlebih dahulu.
2. Tambahkan input kategori di Python.
3. Perbarui INSERT.
4. Perbarui SELECT dan output.
5. Jika edit kategori diperlukan, perbarui UPDATE.

Starter migration:

```sql
ALTER TABLE transactions
ADD COLUMN kategori VARCHAR(50) NOT NULL DEFAULT 'Lainnya';
```

Expected:

```text
1 | Kopi Susu | Makanan | Rp25000
```

## 🌳 EXPLORE — Total seluruh pengeluaran

Gunakan query berikut di MySQL, lalu panggil dari Python:

```sql
SELECT SUM(total) AS grand_total
FROM transactions;
```

Expected dengan tiga data awal:

```text
Total seluruh pengeluaran: Rp75000
```

## Reflection

1. Sebelum latihan, transaksi tinggal di mana?
2. Setelah menggunakan MySQL, transaksi tinggal di mana?
3. Apa pekerjaan Python?
4. Apa pekerjaan SQL?
5. Apa pekerjaan MySQL?
6. Mengapa list tetap berguna setelah ada database?
7. Jika data tidak muncul, bagian mana yang kamu cek lebih dahulu?
