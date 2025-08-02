def tong_so_nguyen(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap so nguyen n: "))
uoc = []
for i in range(1, n + 1):
    if n % i == 0 and tong_so_nguyen(sum(int(chuoi) for chuoi in str(i))):
        uoc.append(i)
print("cac uoc co tong la mot so nguyen to lan luot la:", uoc)
