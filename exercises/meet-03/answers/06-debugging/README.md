# Penjelasan Lima Bug

## Bug 1 — Column

Schema memiliki `total`, bukan `nominal`. Perubahan minimum adalah mengganti nama
column pada SELECT. Verifikasi dengan membandingkan query terhadap `setup.sql`.

## Bug 2 — Commit

`execute()` menjalankan INSERT dalam transaction. `db.commit()` membuat perubahan
bertahan setelah connection ditutup. Buktikan dengan SELECT dari connection baru.

## Bug 3 — Tuple

`(id_transaksi)` hanya ekspresi dalam tanda kurung. `(id_transaksi,)` adalah tuple
satu item yang dapat digunakan sebagai parameter connector.

## Bug 4 — Database

Konfigurasi menulis `raincode_expenses`, sedangkan schema bernama
`raincode_expense`. Error terjadi sebelum query CRUD dijalankan.

## Bug 5 — WHERE

Query memakai ID `999`, bukan variable `id_transaksi`. SQL valid, tetapi tidak ada
target yang cocok sehingga `rowcount` adalah 0. Parameter kedua harus memakai ID
yang diminta task.
