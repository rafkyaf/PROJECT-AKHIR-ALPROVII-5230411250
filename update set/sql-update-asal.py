import sqlite3
hwn = sqlite3.connect('database_hewan.db')
choose = hwn.cursor()

choose.execute(
    f"UPDATE HEWAN SET nama_hewan = 'Komodo', asal = 'Nusa Tenggara Timur' WHERE Id_hewan= 3")
hwn.commit()
if choose.rowcount > 0:
    print(f"Data Komodo berhasil diupdate.")
else:
    print(f"Tidak ada data Komodo.")

choose.close()