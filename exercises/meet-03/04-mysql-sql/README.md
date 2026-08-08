# Level 4 — MySQL dan SQL

Sampai sekarang kita adalah programmer yang mengubah list Python. Pada level ini
kita menjadi manusia yang berkomunikasi langsung dengan MySQL menggunakan SQL.

## Urutan

1. Jalankan `setup.sql` untuk membuat database dan table.
2. Kerjakan `exercise.sql` satu challenge setiap kali.
3. Gunakan `baca_query.sql` untuk latihan prediksi.
4. Perbaiki query pada `debug_query.sql`.

## Menjalankan lewat MySQL Workbench

1. Buka koneksi lokal.
2. Pilih **File → Open SQL Script**.
3. Buka `setup.sql`.
4. Klik ikon petir untuk menjalankan seluruh script.
5. Refresh panel Schemas.

## Expected schema

```text
raincode_expense
└── transactions
    ├── id     INT, PRIMARY KEY, AUTO_INCREMENT
    ├── nama   VARCHAR(100), NOT NULL
    └── total  DECIMAL(12,2), NOT NULL
```

## Checkpoint

- [ ] Bisa menjalankan `CREATE DATABASE` dan `CREATE TABLE` dari starter.
- [ ] Bisa melakukan INSERT dan SELECT.
- [ ] Bisa melakukan UPDATE dengan WHERE.
- [ ] Bisa melakukan DELETE dengan WHERE.
- [ ] Bisa memprediksi hasil SELECT sederhana.
- [ ] Bisa membandingkan query dengan schema ketika ada error.
