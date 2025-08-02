def so_doi_xung(n):
    n = str(n)
    if n == ''.join(reversed(n)):
        return True
    else:
        return False
so = int(input("nhap so nguyen can kiemtra: "))
if so_doi_xung(so):
    print("la so doi xung")
else:
    print("ko la so doi xung")