def so_hoan_hao(s):
    tong = 0
    for a in range(1, s):
        if s % a == 0:
            tong = tong + a
    if tong == s:
        return True
    else:
        return False
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
for i in range(a, b + 1):
    if so_hoan_hao(i):
        print(i, end=" ")