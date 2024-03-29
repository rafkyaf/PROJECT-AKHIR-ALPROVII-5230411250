import sqlite3
hwn = sqlite3.connect('database_hewan.db')

hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Orangutan', 'Mamalia', 'Sumatera', 14000, 2021)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Harimau Sumatera', 'Mamalia', 'Sumatera', 400, 2020)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Komodo', 'Reptil', 'Nusa Tenggara', 3000, 2019)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Anoa', 'Mamalia', 'Sulawesi', 5000, 2022)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Badak Jawa', 'Mamalia', 'Jawa', 72, 2021)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Kuskus', 'Mamalia', 'Papua', 50, 2020)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Trenggiling', 'Mamalia', 'Sumatera', 90, 2022)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Burung Cendrawasih', 'Burung', 'Papua', 45, 2021)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Penyu Hijau', 'Reptil', 'Nusa Tenggara Timur', 20, 2022)")
hwn.execute("INSERT INTO HEWAN ('nama_hewan', 'jenis', 'asal', 'jml_sekarang', 'thn_ditemukan') VALUES ('Gajah Sumatera', 'Mamalia', 'Sumatera', 2500, 2023)")
hwn.commit()

hwn.close()