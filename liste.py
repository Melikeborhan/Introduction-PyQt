# liste1 = [1, 2, 3]
# demet = (1, 2, 3)

# liste1.append(4)
# # demet.append(4)#boyle yapılmaz!!!
# demet = (1, 2, 3, 4)
# # tuple bir kere tanımladıtan sonra bır daha değştirilmez  ama yeniden tanımlamnabılır.


# liste = [print, 2, 9]
# # liste[0] = a
# liste[0]("merhaba")
# # print(liste)

############bunlar bos liste için olan kullanımıdır################
# liste = []
# liste = list()
######################


# liste = [1, 2, 3, 4, 5, 6, 7, 9]
# print(id(liste[0]))

# liste3 = [1, 2, 3, 4, 5, 6, 7, 9]
# liste3.sort()  # sort sıralamalar için kullanılır


# liste3.reverse()  # tam tersıne sıralar
# # append her zaman sondan ekler

# # bastan eklemek vs istersen
# liste3.insert(0, "B")
# print(liste3)
# # extend iki listeyi birleştirme
# # pop silip atar

# c
# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(liste[-4:4:-1])
# print(liste[5:7])
# print(liste[6:4:-1])
# print(liste[::-1])
# print(liste[::-1])


# liste5 = [1.4, "a", "B", 4, 5, 6, True, 8, "k", 10]
# print(liste5[-4:-1])
# print(liste5[8:-5:-1][::-1])
# print(liste5[8:-5:-1])
# print(liste5[9:-5])
# print(liste5[:10][::-1])

# veri = [1, 2, 3, 4, 5]
# a, b = veri[1:3]
# print(a, b)


# a = "\N{Heavy Black Heart}"
# print(a)


# s = "C:/Users/borha/desktop/PYTHON/nesne.py"

# elemanlar = s.split("/")
# dizinler = elemanlar[-1]
# dizin_sayısı = len(dizinler)
# print(dizin_sayısı)

# print(len(s.split("/")))
# print(list(s.split("/")[:-1]))

# s = "Python rocks!"

# s_list = list(s)
# str = "rocks"
# str_index = s.index(str)  # 7
# str_lenght = len(str)  # 5

# del s_list[str_index : str_index + str_lenght]

# print("".join(s_list))
# "Python !" sonucunu verir.


# Format kullanarak aynı stringleri birleştirelim.
# name = "John"
# surname = "Doe"
# age = 25
# print("My name is {} {} and I am {} years old.".format(name, surname, age))


# # Formatlama sırasında sayılar için virgülden sonrası kaç basamak olacağını belirtebiliriz.
# pi = 3.141592653589793
# print('Pi sayısı: {:.2f}'.format(pi))


# f string ile az önceki örneğin aynısını yapalım.
# Ama bu sefer ad ve soyad stringlerini büyük harfe çevirelim.
name = "John"
surname = "Doe"
age = 25
print(f"My name is {name.upper()} {surname.upper()} and I am {age} years old.")


# Bir range oluşturalım ve printleyelim.
r = range(10)
print(list(r))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# For döngüsü örneği
for x in [1, 2]:
    print(x)
print("bitti.")
# 1
# 2
# bitti.


# Range fonksiyonunu kullanarak for döngüsü örneği
for x in range(4, 6):
    alan = x * x
    print(alan)
print("bitti.")
# 16
# 25
# bitti.


# enumerate ile for döngüsü örneği
data = [1, -2, 3, -4, 5]
for index, eleman in enumerate(data):
    if eleman < 0:
        data[index] = 0
print(data)
# [1, 0, 3, 0, 5]


# enumerate ile for döngüsü örneği
data = [[1, -2], [3, -4]]
for x, y in data:
    print(x, y)
# 1 -2
# 3 -4


data = [[1, -2], [3, -4]]
for x, y in data:
    print(f"{x=},{y=}")
# x=1,y=-2
# x=3,y=-4
