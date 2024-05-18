data = []
for i in range(10):
  nilai = float(input("Masukan nilai ke-" + str(i+1) + ": "))
  data.append(nilai)

# Menghitung mean
mean = sum(data) / len(data)

# urutkan data
data.sort()

# median (nilai tengah)
if len(data) % 2 == 0:
  median = (data[len(data) // 2-1] + data[len(data) // 2]) / 2
else:
  median = data[len(data) // 2]

# modus (banyak nilai muncul)
from collections import Counter

modus = None
jumlah_frekuensi = 0

for nilai, frekuensi in Counter(data).most_common():
  if frekuensi > jumlah_frekuensi:
    modus = nilai
    jumlah_frekuensi = frekuensi

# output
print("Mean : ", mean)
print("Median (nilai tengah) : ", median)
print("Modus (banyak nilai muncul) : ", modus)