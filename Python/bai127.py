def so_le(n):
    if n % 2 != 0:
        return True
    else:
        return False
n = int(input("nhap so nguyen duong n: "))
uoc = []
for i in range(1, n + 1):
    if n % i == 0 and so_le(i):
        uoc.append(i)
print("tong cac uoc so le cua n la:", sum(uoc))
