def tong_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap so nguyen duong n: "))
so_nguyen_to = []
for i in range(1, n):
    if tong_nguyen_to(sum(int(ch) for ch in str(i))):
        so_nguyen_to.append(i)
print("cac so co tong la mot so be hon n la:", so_nguyen_to)
