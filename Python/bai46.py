chuoi = input("nhap chuoi: ")
chu = 0
so = 0
ky_tu = 0
for cha in chuoi:
    if cha.isalpha():
        chu = chu + 1
    elif cha.isdigit():
        so = so + 1
    else:
        ky_tu = ky_tu + 1
print("so chu cai:", chu)
print("so chu so:", so)
print("so ky tu dac biet:",ky_tu)