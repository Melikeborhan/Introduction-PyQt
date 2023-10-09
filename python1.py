# system_username = "melike"
# system_parola = "1234"

# username = input("kullanaıcı adı girin: ")
# parola = input("kullanaıcı parola girin: ")

# print(username == system_username and parola == system_parola)
# # admin' or '1'='1#parola=''  güvenlik açığı


from decimal import Decimal, getcontext


x = Decimal("0.1")
y = Decimal("0.1")
z = Decimal("0.2")


print(x + y == z)
