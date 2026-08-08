# Penjelasan Final Challenge

Solution memisahkan satu tanggung jawab ke setiap function. Setiap function
membuka connection saat diperlukan dan selalu menutup resource melalui `finally`.

Hal penting untuk dibandingkan:

- value input dikirim melalui params;
- mutation selalu diikuti commit;
- `rowcount` membedakan berhasil dan ID tidak ditemukan;
- input angka ditangani tanpa membuat menu berhenti;
- loop menu berhenti hanya ketika user memilih 5.

Alternatif yang juga benar adalah memakai satu connection selama menu berjalan,
selama connection tersebut tetap ditutup ketika aplikasi selesai.
