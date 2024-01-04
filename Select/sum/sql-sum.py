import sqlite3
hwn = sqlite3.connect('database_hewan.db')
choose = hwn.cursor()

choose.execute("SELECT SUM(jml_sekarang) FROM HEWAN")
total_hewan = choose.fetchone()[0]

print(f"Total populasi hewan langka saat ini: {total_hewan}")

hwn.close()