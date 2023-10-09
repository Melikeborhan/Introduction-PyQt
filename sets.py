# set için süslğ parantez kullanılır.

# Set oluşturma
set1 = set([1, 2, 3])
set2 = {1, 2, 3}
print(set1, set2)
# {1, 2, 3} {1, 2, 3}


# Listeyi set e çevirme
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
set3 = set(liste)
print(set3)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# EĞER BİR YERDE UNİQUE ETMEK İSTİYORSAK ORDA SET KULLANLIR


# Tekrarlı eleman olan bir listeyi sete çevirelim
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
set4 = set(liste)
print(set4)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


string = "python"

set5 = set(string)
print(set5)
# Python setleri, benzersiz öğelerin koleksiyonunu temsil eder. Setler, aynı öğeyi birden çok kez içeremezler ve öğeler sırasız bir şekilde saklanır.


# Setlerde disjointness kontrolü. Ortak eleman yoksa True döner.
# Bir veya birden fazla ortak eleman varsa False döner.
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
print(set1.isdisjoint(set2))
# True

# ÖRNEĞİN ORTAK ARKADASLAR BURADA TRUE ILE AYRIK KUME OLDUGUNU ORTAK ARKADAS LMADIGINI GOSTERDI.


# Bir sete eleman eklemek
set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(set1)

# İÇİNE BİR LİSTE EKLENEMEZ ÇÜNKÜ HASHLANABILIR OLMAINDAN DOLAYIDIR.


# import collections

# declaring namedtuple


# from collections import namedtuple

# nikita = Student("stuent")

set1 = {1, 2, 3, 4}
set1.discard(3)  # DİSCARD VARSA SILER YOKSA GECER HATA VERMEZ!!
print(set1)


set5 = {1, 2, 3, 4}
set5.remove(3)  # REMOVE VARSA SILER YOKSA KEYERROR HATASI VERİR!!
print(set5)


# list1 = {1, 2, 3, 4, 5}
# list2 = {1, 2, 6, 7, 8}

# # print(len(z) - len(x))
# # print(set(z) - set(x))

# for x in list1:
#     if x not in liste2:
#         print(x)


# sonuc = set(list1) - set(liste2)
# print(sonuc)


# # List Comprehension ile tuple içindeki sayıların karesinin listesi
# sayilar = (1, 2, 3, 4, 5)
# liste = [sayi**2 for sayi in sayilar]
# print(liste)
# # [1, 4, 9, 16, 25]
#################################
sayilar = [1, 2, 3, 4, 5]
demet = (sayi**2 for sayi in sayilar if sayi % 2 == 0)
print(demet)

for i in demet:
    print(i)
# 4
# 16
################################

# sayilar = (1, 2, 3, 4, 5, 8, 9)
# liste = [sayi**2 for sayi in sayilar]
# print(liste)


# Comprehension ile aynı sözlüğü oluşturalım.
# urunler = ["elma", "armut", "muz", "kiraz"]
# fiyatlar = [5, 6, 7, 0]
# sozluk = {urunler[i]: fiyatlar[i] for i in range(len(urunler)) if fiyatlar[i] > 0}
# print(sozluk)
# {'elma': 5, 'armut': 6, 'muz': 7}


products = ["Coca-Cola", "Toyota", "Google", "Microsoft"]
price = [25, 20000, 30, 500]
sozluk = {products[i]: price[i] for i in range(len(products)) if price[i] > 0}
print(sozluk)


sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tekler = {sayi for sayi in sayilar if sayi % 2 != 0}
print(tekler)
# {1, 3, 5, 7, 9}


# Bir listedeki sayıların çift olanlarını bulalım ve listemizdeki elemanları benzersiz yapalım.
sayilar = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
ciftler = {sayi for sayi in sayilar if sayi % 2 == 0}
sayilar2 = list(ciftler)
print(sayilar2)
# [2, 4, 6, 8, 10]


markalar = [
    "Apple",
    "Samsung",
    "Nike",
    "Coca-Cola",
    "Toyota",
    "Google",
    "Microsoft",
    "Amazon",
    "Adidas",
    "BMW",
]


# set5 = {1, 2, 3, 4}

# print(set5.remove(9))  # REMOVE VARSA SILER YOKSA KEYERROR HATASI VERİR!!
# # print(set5)


# urunler = ["elma", "armut", "muz", "kiraz"]
# fiyatlar = [5, 6, 7, 0]
# try:
#     sozluk = {urunler[i]: fiyatlar[i] for i in range(len(urunler)) if fiyatlar[i] > 0}
# except Keyerror as ex:
#     print(f'hata: {ex}')




*args ıstedıgın kadar parametre gırebılırsın demektır.









