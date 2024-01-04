import sqlite3
hwn = sqlite3.connect('database_hewan.db')
choose = hwn.cursor()

jenis = 'Mamalia'  # ID pegawai yang akan dihapus
choose.execute(f"DELETE FROM HEWAN WHERE jenis = 'Mamalia'")
hwn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if choose.rowcount > 0:
    print(f"Data hewan dengan jenis {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data hewan dengan jenis {jenis}.")

# Menutup koneksi
hwn.close()
# Belum benar