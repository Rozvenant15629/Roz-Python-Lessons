n = int(input("nhap so nguyen can kiem tra: "))
maxval = 0
while n > 0:
    a = n % 10
    if a > maxval:
        maxval = a
    n = n // 10
print("chu so lon nhat trong cac so do la:", maxval)