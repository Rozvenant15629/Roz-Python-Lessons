n = int(input("nhap so nguyen duong can dem: "))
chan = 0
le = 0
while n > 0:
    a = n % 10
    if a % 2 == 0:
        chan = chan + 1
    else:
        le = le + 1
    n = n // 10
print("so chu so chan va le lan luot la:", chan, "va", le)