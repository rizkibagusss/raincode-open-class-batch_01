"""Solution final challenge RainCode Expense Tracker CLI."""

from decimal import Decimal, InvalidOperation

from database import get_connection


def lihat_transaksi():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nama, total FROM transactions ORDER BY id")
        transactions = cursor.fetchall()

        print("\n=== DAFTAR TRANSAKSI ===")
        if not transactions:
            print("Belum ada transaksi.")
            return

        for transaction in transactions:
            print(
                f"{transaction['id']} | {transaction['nama']} | "
                f"Rp{transaction['total']:.0f}"
            )
    finally:
        cursor.close()
        db.close()


def tambah_transaksi():
    nama = input("Nama: ").strip()
    try:
        total = Decimal(input("Total: ").strip())
    except InvalidOperation:
        print("Total harus berupa angka.")
        return

    if not nama or total < 0:
        print("Nama wajib diisi dan total tidak boleh negatif.")
        return

    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO transactions (nama, total) VALUES (%s, %s)",
            (nama, total),
        )
        db.commit()
        print(f"Transaksi tersimpan dengan ID {cursor.lastrowid}.")
    finally:
        cursor.close()
        db.close()


def edit_transaksi():
    try:
        id_transaksi = int(input("ID yang diedit: ").strip())
        total_baru = Decimal(input("Total baru: ").strip())
    except (ValueError, InvalidOperation):
        print("ID dan total harus berupa angka.")
        return

    if total_baru < 0:
        print("Total tidak boleh negatif.")
        return

    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            "UPDATE transactions SET total = %s WHERE id = %s",
            (total_baru, id_transaksi),
        )
        db.commit()
        print("Transaksi diperbarui." if cursor.rowcount else "ID tidak ditemukan.")
    finally:
        cursor.close()
        db.close()


def hapus_transaksi():
    try:
        id_transaksi = int(input("ID yang dihapus: ").strip())
    except ValueError:
        print("ID harus berupa angka.")
        return

    if input("Yakin hapus? (y/n): ").strip().lower() != "y":
        print("Penghapusan dibatalkan.")
        return

    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            "DELETE FROM transactions WHERE id = %s",
            (id_transaksi,),
        )
        db.commit()
        print("Transaksi dihapus." if cursor.rowcount else "ID tidak ditemukan.")
    finally:
        cursor.close()
        db.close()


def tampilkan_menu():
    print("\n=== RAINCODE EXPENSE TRACKER ===")
    print("1. Lihat transaksi")
    print("2. Tambah transaksi")
    print("3. Edit transaksi")
    print("4. Hapus transaksi")
    print("5. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            lihat_transaksi()
        elif pilihan == "2":
            tambah_transaksi()
        elif pilihan == "3":
            edit_transaksi()
        elif pilihan == "4":
            hapus_transaksi()
        elif pilihan == "5":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
