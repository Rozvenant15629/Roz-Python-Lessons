def so_hoan_hao(n):
    uoc = []
    for i in range(1, n):
        if n % i == 0:
            uoc.append(i)
    if sum(uoc) == n:
        return print("so vua nhap vao la mot so hoan hao")
    else:
        return print("so vua nhap vao khong la mot so hoan hao")
n = int(input("nhap so nguyen duong n: "))
so_hoan_hao(n)