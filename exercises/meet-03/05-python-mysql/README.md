# Level 5 — Python Bertemu MySQL

Python tidak menjalankan SQL sendiri. `mysql-connector-python` membuka connection
dan mengirim query ke MySQL Server.

## Sebelum mulai

Jalankan setup dan SQL CRUD di folder sebelumnya. Dari folder `meet-03`:

```powershell
Copy-Item .env.example .env
python -m pip install -r requirements.txt
python 05-python-mysql/01_connection.py
```

## Urutan wajib

1. `01_connection.py` — buktikan koneksi dahulu.
2. `02_read.py` — mulai dari operation paling aman.
3. `03_create.py` — temukan mengapa commit diperlukan.
4. `04_update.py` — isi parameter dengan urutan benar.
5. `05_delete.py` — lengkapi query berdasarkan ID.
6. `06_baca_kode.py` — jangan coding; jelaskan alurnya.

## Model mental

```text
Python
→ get_connection()
→ cursor
→ cursor.execute(query, params)
→ MySQL memproses SQL
→ fetchall() / commit()
→ Python menerima list of dictionaries
```

## Checkpoint

- [ ] Bisa membuka dan menutup connection.
- [ ] Bisa membuat cursor dictionary.
- [ ] Bisa menjalankan SELECT dan fetchall.
- [ ] Memahami fungsi commit pada perubahan data.
- [ ] Mengirim value terpisah dari query menggunakan `%s`.
- [ ] Bisa menghubungkan hasil MySQL dengan list/dict Meet 01.
