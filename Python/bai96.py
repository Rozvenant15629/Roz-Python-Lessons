def so_dao(n):
    chuoi = str(n)
    if chuoi == chuoi[::-1]:
        return True
    else:
        return False
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
if a > b:
    a, b = b, a
print("cac so thuan nghich nam trong khoang tu", a, "den", b, "la:")
for i in range(a, b + 1):
    if so_dao(i):
        print(i, end=" ")