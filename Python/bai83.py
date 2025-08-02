def so_hoan_hao(n):
    tong = 0
    for a in range(1, n):
        if n % a == 0:
            tong = tong + a
    if tong == n:
        return True
    else:
        return False
n = int(input("nhap mot so nguyen duong can kiem tra: "))
if so_hoan_hao(n):
    print("la so hoan hao")
else:
    print("khong la so hoan hao")
