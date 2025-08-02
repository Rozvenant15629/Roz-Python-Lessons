def so_chinh_phuong(n):
    can = n ** 0.5
    if can * can == n:
        return True
    else:
        return False
n = int(input("nhap so nguyen duong n: "))
uoc = []
for i in range(1, n + 1):
    if n % i == 0 and so_chinh_phuong(i):
        uoc.append(i)
print("cac uoc cua n la so chinh phuong lan luot la:", uoc)