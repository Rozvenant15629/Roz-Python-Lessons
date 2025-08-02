print("1. cong")
print("2. tru")
print("3. nhan")
print("4. chia")
chon = input("chon phep tinh (1-4): ")
a = int(input("nhap so a: "))
b= int(input("nhap so b: "))
if chon == "1":
    print("ket qua:", a + b)
if chon == "2":
    print("ket qua:", a - b)
if chon == "3":
    print("ket qua:", a * b)
if chon == "4":
    print("ket qua:", round(a / b, 2))