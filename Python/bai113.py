def tong_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap so nguyen duong n: "))
uoc = []
for b in range(1, n + 1):
    if n % b == 0 and tong_nguyen_to(sum(int(chuoi) for chuoi in str(b))):
        uoc.append(b)
print("cac uoc co tong cac chu so la mot so nguyen to la:", uoc)