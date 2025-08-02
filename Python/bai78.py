def so_nguyen_duong(s):
    if s > 0:
        return True
    else:
        return False
so = int(input("nhap so can kiem tra: "))
if so_nguyen_duong(so):
    print("la so nguyen duong")
else:
    print("la so nguyen am")