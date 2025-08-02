xuan = None
while True: 
    n = int(input("nhap gia tri n: "))
    if n == -1:
        break
    if xuan is None or n < xuan:
        xuan = n
print("so co giatri nho nhat trong cac so la:", xuan)