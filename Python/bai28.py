max_val = None
while True:
    n = int(input("nhap so n: "))
    if n == -1:
        break
    if max_val is None or n > max_val:
        max_val = n
print("so lon nhat trong cac so la:", max_val)