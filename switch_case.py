def kategori_penjualan(jumlah):
    switcher={
        jumlah <= 50 : "Rendah",
        50 <= jumlah < 80 : "Sedang",
        80 <= jumlah < 100 : "Menengah Atas",
        jumlah == 100 : "Tinggi"
    }
    return switcher.get(True, "Jumlah tidak valid")

print(kategori_penjualan(20))
print(kategori_penjualan(81))
print(kategori_penjualan(150))
