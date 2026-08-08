# 05 — Frontend Berkomunikasi dengan Backend

Bagian ini mendampingi halaman 41–48 modul dan merupakan evolusi demo pertama.

```text
Sebelum: form → array JavaScript → table → hilang saat refresh
Sekarang: form → HTTP → Flask → service/query → MySQL → JSON → table
```

## Jalankan

```powershell
pip install -r requirements.txt
Copy-Item .env.example .env
# Isi kredensial MySQL
python app.py
```

Buka `http://localhost:5000`.

## Method, route, dan query

| Method | URL | CRUD | Service | SQL |
|---|---|---|---|---|
| GET | `/api/transactions` | Read | `get_all()` | `SELECT` |
| POST | `/api/transactions` | Create | `create()` | `INSERT` |
| PATCH | `/api/transactions/<id>` | Update | `update()` | `UPDATE ... WHERE id` |
| DELETE | `/api/transactions/<id>` | Delete | `delete()` | `DELETE ... WHERE id` |

HTML form native paling umum memakai GET dan POST. JavaScript `fetch()` membantu
mengirim PATCH dan DELETE serta memperbarui table tanpa reload penuh.

## Telusuri satu CREATE

1. JavaScript membentuk `{"nama": "Kopi Susu", "total": 25000}`.
2. POST membawa JSON ke `/api/transactions`.
3. Route Flask membaca `request.get_json()`.
4. Service memvalidasi data dan memilih query `INSERT`.
5. `db.execute()` mengirim query berparameter dan melakukan commit.
6. Service membaca row baru berdasarkan `lastrowid`.
7. Flask mengirim JSON dengan status `201 Created`.
8. JavaScript menjalankan GET dan merender table terbaru.

Mintalah peserta refresh halaman. Data tetap ada karena sumber table sekarang
MySQL, bukan array browser.

