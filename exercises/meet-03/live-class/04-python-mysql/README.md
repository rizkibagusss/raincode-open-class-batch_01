# 04 — Python Berkomunikasi dengan MySQL

Bagian ini mendampingi halaman 30–40 modul. Python tidak memahami protokol MySQL
sendiri. Package `mysql-connector-python` menjadi penerjemah antara kode Python
dan server MySQL.

## Setup

```powershell
pip install -r requirements.txt
Copy-Item .env.example .env
# Isi DB_PASSWORD pada .env
python crud_demo.py
```

Jalankan `../03-database-mysql/01-schema.sql` lebih dahulu.

## Alur satu query

```text
fungsi CRUD
→ db.execute(query, params)
→ buka connection
→ buat cursor(dictionary=True)
→ cursor.execute(query, params)
→ MySQL menjalankan SQL
→ fetch hasil SELECT atau commit perubahan
→ tutup cursor dan connection
```

Query sengaja ditulis di setiap fungsi CRUD agar peserta melihat API mana yang
memanggil SQL apa. `database.py` hanya mengurus mekanisme koneksi dan eksekusi.

```python
# Benar: value dikirim terpisah dari syntax SQL
db.execute("SELECT * FROM transactions WHERE id = %s", (transaction_id,))

# Hindari: input menjadi bagian dari syntax SQL
db.execute(f"SELECT * FROM transactions WHERE id = {transaction_id}")
```

- `fetch="one"` mengambil satu row dictionary atau `None`.
- `fetch="all"` mengambil `list[dict]`.
- `INSERT`, `UPDATE`, dan `DELETE` di-commit agar perubahan permanen.
- Kegagalan mutation di-rollback agar transaction tidak setengah selesai.

Sebelum lanjut, peserta harus mampu menunjuk: koneksi dibuat di `database.py`,
sedangkan query CREATE/READ/UPDATE/DELETE terlihat di `crud_demo.py`.

