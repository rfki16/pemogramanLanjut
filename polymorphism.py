class Pelanggan:
    def penagihan(self):
        pass

class PelangganRetail(Pelanggan):
    def penagihan(self):
        return "Proses penagihan untuk Pelanggan Retail"

class PelangganBisnis(Pelanggan):
    def penagihan(self):
        return "Proses penagihan untuk Pelanggan Bisnis"

class PelangganGrosir(Pelanggan):
    def penagihan(self):
        return "Proses penagihan untuk Pelanggan Grosir"


obj_a = PelangganGrosir()
obj_b = PelangganRetail()

print(obj_b.penagihan())
#
# for obj in [obj_a, obj_b]:
#     print(obj.penagihan())

