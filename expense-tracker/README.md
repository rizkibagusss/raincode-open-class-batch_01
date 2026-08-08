# Expense Tracker

Project utama RainCode Open Class — aplikasi pencatat pengeluaran
yang tumbuh selama empat pertemuan, dari `app.py` 6 baris di
[exercises/meet-03](../../exercises/meet-03) sampai versi rasa-industri
yang dibaca di [exercises/meet-04](../../exercises/meet-04).

Folder ini berisi dua versi, untuk dua tujuan berbeda:

| Folder | Isi | Kapan Dipakai |
|---|---|---|
| [starter](starter) | Versi MySQL sederhana: Route → Service/query → `db.execute()` | Untuk melihat hubungan API dan query secara langsung sebelum belajar Repository Pattern |
| [final](final) | Versi lengkap yang sudah jalan, ditulis rasa-industri | Bahan baca di `exercises/meet-04`, dan pembanding setelah kamu selesai (atau mentok) di `starter` |

## Kenapa Dua Versi?

Ini pola yang sama dengan `challenge` → `solution` di setiap
`exercises/meet-XX`, hanya levelnya satu project utuh:

- **`starter`** menunjukkan query langsung di Service agar hubungan antara API,
  query, dan hasil database mudah ditelusuri.
- **`final`** adalah kunci jawaban sekaligus bahan latihan membaca
  kode di `meet-04` — kamu **membacanya**, bukan mengeditnya.

Pelajari `starter` terlebih dahulu, lalu bandingkan dengan `final` untuk melihat
mengapa aplikasi yang lebih besar memindahkan SQL ke Repository.

## Bukan Duplikat `exercises/meet-03`

`exercises/meet-03/01` sampai `11` mengajarkan fondasi Flask & SQL
selangkah demi selangkah. Project ini melanjutkan fondasi tersebut dengan MySQL.
`starter` di sini berbeda: aplikasinya lengkap, tetapi struktur databasenya
sengaja dibuat lebih pendek agar setiap route mudah dipasangkan dengan query.

RainCode Open Class · Understand before memorizing.
