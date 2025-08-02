def so_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input("nhap so nguyen n: "))
uoc = []
for a in range(1, n + 1):
    if n % a == 0 and so_chan(sum(int(ch) for ch in str(a))):
        uoc.append(a)
print("so uoc co tong la so chan la:", uoc)