def uoc_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input("nhap so nguyen duong n: "))
uoc = []
for a in range(1, n + 1):
    if n % a == 0 and uoc_chan(a):
        uoc.append(a)
print("cac uoc la mot so chan la:", uoc)
