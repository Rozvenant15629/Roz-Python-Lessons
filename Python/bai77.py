def doi_xung(s):
    if s == ''.join(reversed(s)):
        return True
    else:
        return False
chuoi = input("nhap chuoi: ")
if doi_xung(chuoi):
    print("doixung")
else:
    print("ko doi xung")
