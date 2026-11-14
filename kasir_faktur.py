# Membuat Program Struk Transaksi & Kasir Otomatis

# Membuat variabel untuk input nama pelanggan, total belanja dan persentase diskon
nama_pelanggan = input("Masukkan Nama Pelanggan: ").upper()
total_belanja = float(input("Masukkan Total Belanja: "))
# Membatasi input persentase diskon dari 0 - 100%
while True:
    persentase_diskon = float(input("Masukkan Persentase Diskon: "))
    if persentase_diskon > 100:
        print("Persentase diskon tidak boleh lebih dari 100%! Silakan masukkan ulang.\n")
    elif persentase_diskon < 0:
        print("Persentase diskon tidak boleh kurang dari 0%! Silakan masukkan ulang.\n")
    else:
        break

# Membuat variabel nominal diskon dan total yang harus dibayarkan
nominal_diskon = total_belanja * (persentase_diskon / 100)
total_bayar = total_belanja - nominal_diskon

# Membuat format teks untuk semua nominal uang
frmt_total_awal = f"Rp{total_belanja:,.2f}"
frmt_diskon = f"Rp{nominal_diskon:,.2f}"
frmt_total_bayar = f"Rp{total_bayar:,.2f}"

# Menampilkan struk pembayaran
print("\n" + "=" * 36)
print(f"{'STRUK PEMBAYARAN':^36}")
print("-" * 36)
print(f"{nama_pelanggan:^36}")
print("=" * 36)
print(f"\n{'Total Awal':<16}{frmt_total_awal:>20}")
print(f"{f'Diskon ({persentase_diskon}%)':<16}{frmt_diskon:>20}")
print("-" * 36)
print(f"{'Total Bayar':<16}{frmt_total_bayar:>20}")
print("\n" + "=" * 36)