def so_doi_xung(n):
    n = str(n)
    if n == str(n)[::-1]:
        return True
    else:
        return False
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
for i in range (a, b + 1):
    if so_doi_xung(i):
        print(i, end=" ")