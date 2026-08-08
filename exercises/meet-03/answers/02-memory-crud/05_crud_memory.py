transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
]


def tambah_transaksi(transaction_id, nama, total):
    transactions.append({"id": transaction_id, "nama": nama, "total": total})


def lihat_transaksi():
    for transaction in transactions:
        print(f"{transaction['id']} | {transaction['nama']} | Rp{transaction['total']}")


def ubah_total(transaction_id, total_baru):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transaction["total"] = total_baru
            return True
    return False


def hapus_transaksi(transaction_id):
    for index, transaction in enumerate(transactions):
        if transaction["id"] == transaction_id:
            transactions.pop(index)
            return True
    return False


tambah_transaksi(3, "Transport", 15000)
ubah_total(1, 30000)
hapus_transaksi(2)
lihat_transaksi()
