# 07 — Debugging Berdasarkan Layer

Bagian ini mendampingi halaman 50–51 modul.

```text
Browser/JavaScript → HTTP/Flask → Python/validation → Connector → SQL/MySQL
```

## Metode lima langkah

1. Reproduksi aksi yang selalu memunculkan masalah.
2. Baca status HTTP, response, atau pesan error paling bawah.
3. Temukan file/baris pertama yang berasal dari kode kita.
4. Tentukan layer gagal dan periksa nilai tepat sebelum gagal.
5. Perbaiki satu penyebab, ulangi aksi, lalu buktikan hasilnya.

Untuk error koneksi, cek service MySQL, host, port, database, user/password,
permission, dan `.env`. Untuk error query, bandingkan nama table/column dengan
`01-schema.sql`. Untuk hasil yang salah, cek urutan parameter, `WHERE`, mode
fetch, `rowcount`, commit, dan proses reload data di UI.

Sebelum `UPDATE` atau `DELETE`, gunakan `SELECT` dengan `WHERE` yang sama:

```sql
SELECT * FROM transactions WHERE id = 7;
DELETE FROM transactions WHERE id = 7;
```

Buka `bug-cards.md`. Pada setiap kasus, sebutkan layer, bukti yang perlu dilihat,
perbaikan minimum, dan cara membuktikan perbaikannya.

