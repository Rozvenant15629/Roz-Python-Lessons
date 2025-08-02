def so_nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int( n ** 0.5 ) + 1):
        if n % a == 0:
            return False
    return True
a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
for i in range( a, b + 1):
    if so_nguyen_to(i):
        print(i, end = " ")