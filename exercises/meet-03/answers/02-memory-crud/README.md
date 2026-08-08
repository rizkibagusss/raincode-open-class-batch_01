# Penjelasan CRUD Memory

- CREATE memakai `append()` untuk menambah dictionary.
- READ memakai loop karena jumlah item dapat berubah.
- UPDATE mencari ID agar tidak bergantung pada posisi list.
- DELETE dapat memakai list comprehension atau mencari index lalu `pop()`.

Alternatif DELETE di solution gabungan memakai `enumerate()` agar index target
tersedia. Keduanya benar untuk tujuan latihan ini.

Data tetap sementara: source code membuat list awal yang sama setiap program
dimulai kembali.
