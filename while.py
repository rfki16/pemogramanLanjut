listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

# WHILE DENGAN BREAK
city = input("Masukan kota yang ingin dicari : ")
i = 0

while i < len(listKota):
    if listKota[i].lower() == city.lower():
        print("ketemu di index - ", i)
        break
    else:
        print('bukan',listKota[i])
        i += 1
else:
        print("maaf, kota yang anda cari tidak ada")

