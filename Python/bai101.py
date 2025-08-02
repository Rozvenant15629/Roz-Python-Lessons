def so_nguyen_to(s):
    if s < 2:
        return False
    for a in range(2, int(s ** 0.5) + 1):
        if s % a == 0:
            return False
    return True
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    if so_nguyen_to(i):
        print(i, end=" ")