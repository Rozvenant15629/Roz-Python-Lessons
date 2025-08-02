n = int(input("nhap so nguyen duong: "))
dem = 0
while n > 0: 
    n = n // 10
    dem = dem + 1
print("so cac chu so cua so nguyen duong la:", dem)