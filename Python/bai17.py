n = int(input("nhap so can kiem tra: "))
if n < 2:
    print(n, "khong phai la so nguyen to")
else:
    xuan = 0
    for a in range(1 , n + 1):
        if n % a == 0:
            xuan = xuan + 1
    if xuan == 2:
        print(n, "la so nguyen to")
    else:
        print(n, "khong la so nguyen to")