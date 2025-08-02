n = int(input("nhap giatri n: "))
chan = True
while n > 0:
    a = n % 10
    if a % 2 != 0:
        chan = False
        break
    n = n // 10
if chan == True:
    print("la so toan chan")
else:
    print("la so ko toan chan")  