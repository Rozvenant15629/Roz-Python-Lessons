def so_chinh_phuong(n):
    can = int(n ** 0.5)
    if can * can == n:
        return True
    else:
        return False
n = int(input("nhap so nguyen n: "))
if so_chinh_phuong(n):
    print(n, "la mot so chinh phuong")
else:
    print(n, "khong la mot so chinh phuong")