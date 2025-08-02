def uoc_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap so nguyen n: "))
uoc = []
for b in range(1, n + 1):
    if n % b == 0 and uoc_nguyen_to(b):
        uoc.append(b)
print("cac uoc la so nguyen to la:", uoc)