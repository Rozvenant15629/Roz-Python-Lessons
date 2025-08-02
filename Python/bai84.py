def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, n):
        if n % a == 0:
            return False
        else:
            return True
n = int(input("nhap so nguyen bat ki: "))
if so_nguyen_to(n):
    print("la so nguyen to")
else:
    print("khong la so nguyen to")
