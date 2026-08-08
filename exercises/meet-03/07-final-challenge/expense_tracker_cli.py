"""Starter final challenge RainCode Expense Tracker CLI."""

from decimal import Decimal, InvalidOperation

from database import get_connection


def lihat_transaksi():
    """STEP 2 — tampilkan seluruh transaksi."""
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    try:
        # TODO: SELECT id, nama, total lalu fetchall().
        # TODO: tampilkan empty state atau loop seluruh row.
        pass
    finally:
        cursor.close()
        db.close()


def tambah_transaksi():
    """STEP 3 — tambah satu transaksi."""
    nama = input("Nama: ").strip()
    try:
        total = Decimal(input("Total: ").strip())
    except InvalidOperation:
        print("Total harus berupa angka.")
        return

    # TODO: validasi nama tidak kosong dan total tidak negatif.
    # TODO: buka connection, jalankan INSERT, commit, lalu tutup resource.


def edit_transaksi():
    """STEP 4 — ubah total berdasarkan ID."""
    # TODO: ambil id_transaksi dan total_baru dari input.
    # TODO: jalankan UPDATE ... WHERE id = %s.
    # TODO: gunakan rowcount untuk pesan berhasil/tidak ditemukan.
    pass


def hapus_transaksi():
    """STEP 5 — hapus transaksi berdasarkan ID."""
    # TODO: ambil ID dan minta konfirmasi y/n.
    # TODO: jalankan DELETE ... WHERE id = %s dan commit.
    # TODO: gunakan rowcount untuk pesan hasil.
    pass


def tampilkan_menu():
    print("\n=== RAINCODE EXPENSE TRACKER ===")
    print("1. Lihat transaksi")
    print("2. Tambah transaksi")
    print("3. Edit transaksi")
    print("4. Hapus transaksi")
    print("5. Keluar")


def main():
    """STEP 6 — hubungkan pilihan menu dengan function."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            lihat_transaksi()
        elif pilihan == "2":
            tambah_transaksi()
        # TODO: lanjutkan pilihan 3, 4, dan 5.
        else:
            print("Pilihan belum tersedia atau tidak valid.")


if __name__ == "__main__":
    main()
