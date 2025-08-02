n = int(input("nhap so nguyen n: "))
a = 1
while a < n:
    if a % 3 == 1 and a % 5 == 2:
        print("so do la:", a)
    a = a + 1