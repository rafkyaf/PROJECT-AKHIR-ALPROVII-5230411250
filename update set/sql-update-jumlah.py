import sqlite3
hwn = sqlite3.connect('database_hewan.db')
choose = hwn.cursor()

choose.execute(f"UPDATE HEWAN SET nama_hewan = 'Orangutan', jml_sekarang='900' WHERE Id_hewan= 1")
hwn.commit()

if choose.rowcount > 0:
    print(f"Data Orangutan berhasil diupdate.")
else:
    print(f"Tidak ada data Orangutan.")

choose.close()
