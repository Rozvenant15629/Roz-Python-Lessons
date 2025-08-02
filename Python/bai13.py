nam = int(input("nhap nam can xet: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Nam", nam, "la nam nhuan")
else:
    print("Nam", nam, "khong phai la nam nhuan")