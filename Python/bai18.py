n = int(input("nhap so can tinh tong cac chu so: "))
tong = 0
while n > 0:
    chusocuoi = n % 10
    tong = tong + chusocuoi
    n = n // 10
print("tong cac chu so la:", tong)