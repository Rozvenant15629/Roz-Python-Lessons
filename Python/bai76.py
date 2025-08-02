def lay_am(ds):
    so_am = []
    for so in ds:
        if so < 0:
            so_am.append(so)
    return so_am
ds = list(map(float, input("nhap danh sach cac so can loc: ").split(",")))
print("danh sach cac so am la:", lay_am(ds))