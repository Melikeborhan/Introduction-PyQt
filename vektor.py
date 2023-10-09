class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vektor):
            yeni_x = self.x + other.x
            yeni_y = self.y + other.y
            return Vektor(yeni_x, yeni_y)
        else:
            raise ValueError("Başka bir nesne ile toplama işlemi yapamazsınız.")


# Kullanım örneği:
v1 = Vektor(2, 3)
v2 = Vektor(1, 2)

v3 = v1 + v2  # İki vektörü topluyoruz, v3 yeni bir vektör olacak

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v3: {v3}")  # v3, v1 ve v2'nin toplamı olarak oluşmuş bir vektördür
