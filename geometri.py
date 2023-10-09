class GeometrikSekil:
    def __init__(self):
        self.isim = "Geometrik Şekil"

    def alan_hesapla(self):
        pass


class Dikdortgen(GeometrikSekil):
    def __init__(self, uzunluk, genislik):
        super().__init__()
        self.isim = "Dikdörtgen"
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan_hesapla(self):
        return self.uzunluk * self.genislik


class Ucgen(GeometrikSekil):
    def __init__(self, taban, yukseklik):
        super().__init__()
        self.isim = "Üçgen"
        self.taban = taban
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return (self.taban * self.yukseklik) / 2


class Daire(GeometrikSekil):
    def __init__(self, yaricap):
        super().__init__()
        self.isim = "Daire"
        self.yaricap = yaricap

    def alan_hesapla(self):
        return 3.14 * self.yaricap**2


# Kullanım örnekleri:
dikdortgen = Dikdortgen(5, 4)
ucgen = Ucgen(6, 8)
daire = Daire(3)

print(f"{dikdortgen.isim} Alanı: {dikdortgen.alan_hesapla()}")
print(f"{ucgen.isim} Alanı: {ucgen.alan_hesapla()}")
print(f"{daire.isim} Alanı: {daire.alan_hesapla()}")
