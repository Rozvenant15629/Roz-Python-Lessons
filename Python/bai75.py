def so_chan(ds):
    chan = []
    for so in ds:
        if so % 2 == 0:
            chan.append(so)
    return chan
ds = list(map(int, input("nhap cac so nguyen can kiem tra: ").split(",")))
print("cac so chan la:", so_chan(ds))