n = int(input("nhap so can dao: "))
han = 0
while n > 0:
    xuan = n % 10
    han = ( han * 10 ) + xuan
    n = n // 10 
print("vay so sau khi duoc dao la:", han)