#PROGRAM VALIDASI NILAI
def valid_nilai(nilai) :
    if nilai >= 88:
        print("Kriteria A")
    elif 77 <= nilai < 88:
        print("Kriteria B")
    elif 60 <= nilai < 77:
        print("Kriteria C")
    elif 45 <= nilai < 60:
        print("Kriteria D")
    else:
        print("Kriteria E")


def main():
    try:
        jumlah_nilai = float(input("Masukan jumlah nilai = "))

        valid_nilai(jumlah_nilai)
    except ValueError:
        print("input harus berupa angka")

if __name__ == "__main__":
    main()
