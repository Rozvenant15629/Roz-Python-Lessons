n = int(input("nhap gia tri n: "))
dem = 0
while n > 0:
    a = n % 10
    if a % 2 != 0:
        dem = dem + 1
    n = n // 10
print("so so le la:", dem)