def nguyen_to(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True
n = int(input("nhap so nguyen duong n: "))
ket_qua = []
for i in range(1, n):
    if nguyen_to(i) and nguyen_to(sum(int(ch) for ch in str(i))):
        ket_qua.append(i)
print("cac so be hon n la so nguyen to va co tong cac chu so cung la so nguyen to la:", ket_qua)