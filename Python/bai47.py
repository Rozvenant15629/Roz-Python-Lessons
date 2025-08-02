chuoi = input("nhap chuoi: ")
chu_in = 0
chu_thuong = 0
chu_so = 0
ky_tu = 0
for char in chuoi:
    if char.isupper():
        chu_in = chu_in + 1
    elif char.islower():
        chu_thuong = chu_thuong + 1
    elif char.isdigit():
        chu_so = chu_so + 1
    else:
        ky_tu = ky_tu + 1
print("so chu in la", chu_in)
print("so chu thuong la", chu_thuong)
print("so chu so la:", chu_so)
print("so ky tu la:", ky_tu)