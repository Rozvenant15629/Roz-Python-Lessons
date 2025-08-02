def so_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False 
n = int(input("nhap so nguyen n: "))
if so_fibonacci(n):
    print(n, "la so fibonacci")
else:
    print(n, "khong phai la so fibonacci")