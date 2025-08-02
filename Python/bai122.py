def uoc_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap vao so nguyen duong n: "))
uoc = []
for i in range(1, n + 1):
    if n % i == 0 and uoc_nguyen_to(i) and uoc_nguyen_to(int(str(i)[-1])):
        uoc.append(i)
print("cac uoc thoa man dieu kien lan luot la:", uoc)