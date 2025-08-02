def uoc_thuan_nghich(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = int(input("nhap mot so nguyen duong bat ki: "))
uoc = []
for a in range(1, n + 1):
    if n % a == 0 and uoc_thuan_nghich(a):
        uoc.append(a)
print("cac uoc la so thuan nghich la:", uoc)

