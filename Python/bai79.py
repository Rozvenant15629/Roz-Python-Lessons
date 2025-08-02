def la_chu_cai(s):
    return s.isalpha()
chuoi = input("nhap chuoi can kiem tra: ")
if la_chu_cai(chuoi):
    print("la chuoi toan chu cai")
else:
    print("khong phai la chuoi toan chu cai")