def tong_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
def uoc(i):
    so_uoc = []
    for b in range(1, i + 1):
        if i % b == 0:
            so_uoc.append(b)
    return so_uoc
n = int(input("nhap vao mot so nguyen duong n: "))
dem = 0
for i in range(1, n + 1):
    if tong_nguyen_to(sum(uoc(i))):
        dem = dem + 1
print("so chu so co tong cac uoc cua so do la mot so nguyen to la:", dem)
