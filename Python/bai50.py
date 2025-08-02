n = int(input("nhap so luong phan tu: "))
ds = []
for a in range(n):
    so = int(input(f"nhap so thu {a + 1}:"))
    ds.append(so)
print("danh sach:", ds)
print("tong:", sum(ds))