def uoc_so_le(n):
    if n % 2 != 0:
        return True
    else:
        return False
n = int(input("nhap so nguyen duong n: "))
uoc = []
for a in range(1, n + 1):
    if uoc_so_le(a) and uoc_so_le(sum(int(ch) for ch in str(a))) and n % a == 0:
        uoc.append(a)
print("cac uoc thoa man dieu kien la:", uoc)