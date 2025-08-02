def so_hoan_hao(n):
    uoc = []
    for a in range(1, n):
        if n % a == 0:
            uoc.append(a)
    if sum(uoc) == n:
        return True
    else:
        return False
n = int(input("nhap so nguyen duong n: "))
ketqua = []
for i in range(1, n):
    if so_hoan_hao(i):
        ketqua.append(i)
print("cac so hoan hao be hon n la:", ketqua)