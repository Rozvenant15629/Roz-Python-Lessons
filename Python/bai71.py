def kiem_tra_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input("nhap so nguyen: "))
if kiem_tra_chan(n):
    print("so chan")
else:
    print("so le")
