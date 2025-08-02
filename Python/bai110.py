def uoc_doi_xung(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = int(input("nhap so nguyen duong n: "))
uoc = []
for a in range(1, n + 1):
    if n % a == 0 and uoc_doi_xung(a):
        uoc.append(a)
print("cac uoc la so doi xung lan luot la:", uoc)