# PROGRAM MENGHITUNG BANYAKNYA BILANGAN GENAP DAN GANJIL

def main():
    #fungsi input jumlah bilangan
    jum_bilangan = int(input("Masukan jumlah bilangan : "))

    #agar sistem melampirkan angka dari jumlah bilangan
    bilangan = list(range(1, jum_bilangan + 1))

    #menampilkan angka yang terlampir
    print(f"Terdapat data : {' '.join(map(str, bilangan))}")

    #memanggil fungsi hitung genap ganjil
    genap, ganjil = hitung_genap_ganjil(bilangan)

    #menampilkan output bilangan genap dan ganjil
    print(f"Jumlah bilangan genap : {len(genap)} yaitu {' '.join(map(str, genap))}")
    print(f"Jumlah bilangan ganjil : {len(ganjil)} yaitu {' '.join(map(str, ganjil))}")

#modul menghitung ganjil dan genap
def hitung_genap_ganjil(bilangan1):
    genap = []
    ganjil = []

    for num in bilangan1:
        if num % 2 == 0:
            genap.append(num)
        else:
            ganjil.append(num)

    return genap, ganjil

#menjalankan fungsi main
if __name__ == "__main__" :
    main()