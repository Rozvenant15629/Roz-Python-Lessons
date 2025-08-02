dien = int(input("nhap so dien da su dung: "))
if dien <= 50:
    tien = dien * 1.678
    print("so tien dien la:", round( tien, 2 ))
elif dien <= 100:
    tien = 50 * 1.678 + ( dien - 50 ) * 1.734
    print("so tien dien la:", round( tien, 2 ))
elif dien <= 200:
    tien = 50 * 1.678 + 50 * 1.734 + ( dien - 100 ) * 2.014
    print("so tien dien la:", round( tien, 2 ))
else:
    tien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + ( dien - 200 ) * 2.536
    print("so tien dien la:", round( tien, 2))