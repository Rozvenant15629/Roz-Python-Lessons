def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap so nguyen duong n: "))
uoc = []
for i in range(1, n + 1):
    if n % i == 0 and so_nguyen_to(i):
        uoc.append(i)
print("so cac uoc nguyen to cua so nguyen n la:", len(uoc))