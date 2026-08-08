"""Demo data sementara menggunakan materi Pertemuan 01."""

from decimal import Decimal, InvalidOperation


transactions: list[dict] = []


def tampilkan_table() -> None:
    """Tampilkan seluruh dictionary di dalam list sebagai table terminal."""
    print("\nID | Nama                 | Total Belanja")
    print("---+----------------------+---------------")
    for item in transactions:
        print(
            f"{item['id']:>2} | {item['nama']:<20} | "
            f"Rp {item['total']:>10,.2f}"
        )
    print(f"\nData sementara saat ini: {len(transactions)} row\n")


def tambah_transaksi(nama: str, total: Decimal) -> None:
    """Buat satu record dictionary lalu append ke list."""
    record = {
        "id": len(transactions) + 1,
        "nama": nama,
        "total": total,
    }
    transactions.append(record)


print("DATA SEMENTARA — ketik 'selesai' pada nama untuk berhenti")

while True:
    nama_input = input("Nama transaksi (contoh: Kopi Susu): ").strip()
    if nama_input.lower() == "selesai":
        break
    if not nama_input:
        print("Nama tidak boleh kosong.\n")
        continue

    try:
        total_input = Decimal(input("Total belanja: ").strip())
    except InvalidOperation:
        print("Total belanja harus berupa angka.\n")
        continue

    if total_input < 0:
        print("Total belanja tidak boleh negatif.\n")
        continue

    tambah_transaksi(nama_input, total_input)
    tampilkan_table()

print("Program selesai. List di memory ikut hilang.")
