# While döngüsü örneği
x = 1
while x < 3:
    print(x)
    x += 1  # important!! sureklı sonsuz olmasını engellemıs olur unutmoa
print("bitti.")
# 1
# 2
# bitti.


# Sadece tek basamaklı sayıları yazdıralım.
sayilar = [1, 20, 3, 40, 55, 60, 7, 80, 99, 100]
for sayi in sayilar:
    if sayi > 9:
        continue  # bir sonraki satırı çalıştırmaz tekrar basa dönmesini sağlar.
    print(sayi)
print("bitti.")
# 1
# 3
# 7
# bitti.






# Break while sonsuz döngüsünü kırabilen bir yapıdır.
x = 1
while True:
    print(x)
    x += 1
    if x > 3:
        break
print("bitti.")
# 1
# 2
# 3
# bitti.






# Break ile bir liste içerisinde arama
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bulundu = False
for el in liste:
    if el == 'python':
        bulundu = True
        print('Bulundu')
        break

if not bulundu:
    print('Bulunamadı')
#Bulunamadı






