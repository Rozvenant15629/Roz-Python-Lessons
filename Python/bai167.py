def convert(n, base):
    decimal = int(n, 0)
    if base == 2:
        return format(decimal, "b")
    elif base == 8:
        return format(decimal, "o")
    elif base == 10:
        return str(decimal)
    elif base == 16:
        return format(decimal, "X")
    else:
        return "base not supported!"
a = input("enter first number (can be 0b, 0o, 0x or decimal): ")
base1 = int(input("enter base to convert (2/8/10/16): "))
b = input("enter second number (can be 0b, 0o, 0x or decimal): ")
base2 = int(input("enter base to convert (2/8/10/16): "))
if int(a, 0) > int(b, 0):
    print("First number in decimal base is bigger than second number in decimal base")
else:
    print("First number in decimal base is smaller than second number in decimal base")
print("first number in base", base1, "is:", convert(a, base1))
print("second number in base", base2, "is:", convert(b, base2))