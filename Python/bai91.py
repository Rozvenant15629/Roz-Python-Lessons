def so_hoan_hao(s):
    tong = 0
    for a in range(1, s):
        if s % a == 0:
            tong = tong + a
    if tong == s:
        return True
    else:
        return False
i = int(input("nhap so nguyen can kiem tra: "))
if so_hoan_hao(i):
    print("la mot so hoan hao")
else:
    print("khong la so hoan hao")
    