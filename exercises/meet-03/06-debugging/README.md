# Level 6 — Debugging Challenge

Setiap file di folder ini sengaja mempunyai satu bug. Jangan membuka `answers/`
sebelum mengikuti proses berikut:

```text
1. Jalankan
2. Baca gejala atau error
3. Cari file dan baris yang dicurigai
4. Bandingkan dengan schema/expected result
5. Perbaiki satu hal
6. Jalankan ulang dan buktikan
```

| File | Gejala | Target belajar |
|---|---|---|
| `bug_01_column.py` | Unknown column | Query harus sama dengan schema |
| `bug_02_commit.py` | Data tidak bertahan | Mutation membutuhkan commit |
| `bug_03_tuple.py` | Parameter tidak diterima | Tuple satu item memakai koma |
| `bug_04_database.py` | Unknown database | Configuration juga dapat gagal |
| `bug_05_where.py` | Tidak ada row berubah | WHERE dan params harus menunjuk target |

Untuk setiap bug, jawab:

1. Bagian mana yang kamu curigai?
2. Bukti apa yang diberikan error atau `rowcount`?
3. Apa perubahan minimum yang diperlukan?
4. Bagaimana membuktikan perbaikannya?

## Checkpoint

- [ ] Tidak mengubah banyak bagian sekaligus.
- [ ] Bisa memisahkan error connection, SQL, dan transaction.
- [ ] Menggunakan schema sebagai sumber kebenaran nama column.
- [ ] Menjalankan SELECT setelah mutation untuk verifikasi.
