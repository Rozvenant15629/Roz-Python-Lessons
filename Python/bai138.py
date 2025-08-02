def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap so nguyen duong n: "))
ketqua = []
for i in range(1, n):
    if so_nguyen_to(i):
        ketqua.append(i)
print("cac so nguyen to nho hon so nguyen n la:", ketqua)