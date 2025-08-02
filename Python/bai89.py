def so_doi_xung(n):
    n = str(n)
    if n == ''.join(reversed(str(n))):
        return True
    else:
        return False
n = int(input("nhap so can kiem tra: "))
if so_doi_xung(n):
    print("la so doi xung")
else:
    print("ko la so doi xung")