# PROGRAM MENGHITUNG JUMLAH BILANGAN GANJIL DAN GENAP

def main() :
    input_bilangan = input("Masukan bilangan (pisah dengan koma) : ")

    #list comprehesion
    bilangan = [int(x) for x in input_bilangan.split(',')]

    #inisialisasi variable
    ganjil = []
    genap = []

    #fungsi memisahkan bil ganjil dan genap
    for num in bilangan:
        if num % 2 == 0:
            genap.append(num)
        else:
            ganjil.append(num)

    #output
    print(f"bilangan ganjil = {len(ganjil)} yaitu {', '.join(map(str, ganjil))}")
    print(f"bilangan genap = {len(genap)} yaitu {', '.join(map(str, genap))}")

#run fungsi
if __name__ == "__main__":
    main()


