def so_chinh_phuong(n):
    can = int(n ** 0.5)
    if can * can == n:
        return True
    else:
        return False
def uoc_nguyen_to(i):
    if i < 2:
        return False
    for a in range(2, int(i ** 0.5) + 1):
        if i % a == 0:
            return False
    return True
n = int(input("nhap so nguyen n: "))
uoc = []
if so_chinh_phuong(n):
    for b in range(1, int(n ** 0.5) + 1):
        if n % b == 0 and uoc_nguyen_to(b):
            uoc.append(b)
    print("so uoc so nguyen to phan biet la:", len(set(uoc)), "cac uoc do lan luot la:", uoc)
else:
    print("khong la so chinh phuong:")