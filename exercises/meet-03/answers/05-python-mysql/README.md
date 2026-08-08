# Penjelasan Python–MySQL

- `cursor(dictionary=True)` membuat setiap row mudah dibaca sebagai dictionary.
- `fetchall()` menghasilkan list berisi row-row tersebut.
- `%s` adalah placeholder value milik connector, bukan format string Python.
- Params dipisahkan agar connector memperlakukan input sebagai data.
- INSERT, UPDATE, dan DELETE membutuhkan `db.commit()`.
- Tuple satu item ditulis `(value,)`, dengan koma sebelum penutup.
- `finally` memastikan cursor dan connection ditutup saat berhasil maupun gagal.
