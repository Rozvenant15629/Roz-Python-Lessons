n = int(input("nhap gia tri n: "))
tich = 1
while n > 0:
    a = n % 10
    if a % 2 != 0:
        tich = tich * a
    n = n // 10
print("tich la:", tich)