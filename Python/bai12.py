a = int(input("nhap so a la: "))
b = int(input("nhap so b la: "))
c = int(input("nhap so c la: "))
if a >= b and a >= c:
    print("so lon nhat la: ", a)
elif b >= a and b >= c:
    print("so lon nhat la: ", b)
else:
    print("so lon nhat la: ", c)