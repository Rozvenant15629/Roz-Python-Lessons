n = int(input("nhap so nguyen n: "))
b = 0
while n > 0:
    a = n % 10
    b = b * 10 + a
    n = n // 10
print('so dao la:', b)