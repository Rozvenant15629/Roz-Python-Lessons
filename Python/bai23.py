n = int(input("nhap so nguyen n: "))
a = 1
tong = 0
while a < n:
    if a % 7 == 0:
        tong = tong + a
    a = a + 1
print('tong la: ', tong)