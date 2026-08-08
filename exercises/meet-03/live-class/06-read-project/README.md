# 06 — Cara Membaca Project per Fitur

Bagian ini mendampingi halaman 49 modul. Jangan mencoba memahami semua file
sekaligus. Pilih satu perilaku yang terlihat, lalu ikuti alurnya.

## Latihan: telusuri tombol Simpan

Buka folder `../05-flask-crud`, lalu jawab berurutan:

1. **Tampilan:** elemen form mana yang mengumpulkan `nama` dan `total`?
2. **Event:** listener JavaScript mana yang menangani submit?
3. **Request:** method, URL, header, dan body apa yang dikirim?
4. **Route:** fungsi Flask mana yang menerima request tersebut?
5. **Validation:** kode mana yang menolak nama kosong atau total negatif?
6. **Query:** SQL apa yang dijalankan dan parameter apa yang masuk ke `%s`?
7. **Database:** table serta column mana yang berubah?
8. **Response:** status HTTP dan JSON apa yang kembali?
9. **Render:** fungsi mana yang meminta dan menampilkan data terbaru?

## Peta file

```text
templates/index.html      bentuk form dan table
static/app.js             event, fetch, dan render
app.py                    route HTTP dan response
service.py                validation, aturan, dan query CRUD
database.py               connection, execute, fetch, commit/rollback
03-database-mysql/*.sql   bentuk database dan table
```

Tugas pasangan: satu peserta menjelaskan alur POST sambil peserta lain menunjuk
file dan baris yang menjadi buktinya. Setelah selesai, tukar peran untuk DELETE.

