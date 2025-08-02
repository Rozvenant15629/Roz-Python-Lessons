def nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap mot so nguyen duong n: "))
uoc = []
for b in range(1, n + 1):
    if n % b == 0 and nguyen_to(b) and sum(int(ch) for ch in str(n)) % b == 0:
        uoc.append(b)
print("cac uoc so nguyen to cua n ma tong chu so cua n cung chia het la:", uoc)