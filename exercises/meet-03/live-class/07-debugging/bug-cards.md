# Bug Cards

## A — Data hilang setelah koneksi ditutup

POST memberi status 201, tetapi row tidak ada saat MySQL client dibuka ulang.
`cursor.execute()` berjalan, sedangkan `connection.commit()` terhapus.

- Apakah ini masalah render atau durability transaction?
- Operation mana yang membutuhkan commit?
- Bagaimana membuktikan row benar-benar permanen?

## B — Nama input tidak sama

Frontend mengirim `nominal`, sedangkan service membaca `total`.

- Periksa payload pada Network tab.
- Bandingkan kontrak frontend, validation, dan query.
- Mengapa satu nama field perlu dipakai konsisten?

## C — Unknown column

Query menulis `INSERT INTO transactions (nama, nominal)`, tetapi schema memiliki
column `nama` dan `total`.

- Layer mana yang menghasilkan error?
- File apa yang menjadi sumber kebenaran struktur table?
- Perubahan minimum apa yang benar?

## D — Semua row berubah

```sql
UPDATE transactions SET total = 0;
```

- Bagian penting apa yang hilang?
- SELECT verifikasi apa yang seharusnya dijalankan lebih dahulu?
- Apa akibatnya jika query sudah di-commit tanpa backup?

