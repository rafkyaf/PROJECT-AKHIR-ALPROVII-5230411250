import sqlite3
hwn = sqlite3.connect('database_hewan.db')
choose = hwn.cursor()
choose.execute("SELECT * FROM HEWAN")
row = choose.fetchall()

print("="*118)
print("{:<8} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID Hewan", "Nama Hewan", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Terakhir Ditemukan"))
print("-"*118)

for i in row:
    print("{:<8} {:<20} {:<20} {:<20} {:<20} {:<20}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

hwn.close()