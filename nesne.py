# bir örnek yapalım
# sonuc = (10).__add__(100)  # 10 + 100 için aslında `__add__` metodunu çağırılır.
# print(sonuc)


# # 10 a 100 eklemiş oluyoruz.ve sonuc 110 oluyor yada;

# a = 10
# b = a.__add__(5)
# print(b)

# böyle yaptığımızda ise b 15 çıkar


# def tip_soyle(func):
#     return type(func)


# print(f"Bu fonsiyonun tipi:  {type(5)})


# a = 257
# b = 257

# print(id(a))
# print(id(b))


# liste = [1, 2, 3]
# liste2 = liste
# liste2.append(4)  # liste2 ye 4  eklenır

# print(liste, liste2)  # sonuc 1,2,3,1,2,3,4 oldu


# liste3 = [1, 2, 3, 4, 5, 6, 6, 8, 8, 8, 5, 5, 2, 2, 9, 9, 9]

# setim = set(liste3)
# uniq_liste = list(setim)

# print(uniq_liste)

# liste = [1, 2, 3]
# liste1 = liste

# liste1 = [1, 2, 3, 4]
# print(liste)
# # mutable ınmutable ??


# x = 5
# y = 5
# print(id(x == y))

# d = 4
# e = 4
# print(id(d == e))

# print(id(bool(1)))


#


a = 256
b = 256
print(id(a), id(b))

a = 257
b = 257
print(id(a), id(b))
