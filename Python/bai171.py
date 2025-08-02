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
def symmetric(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = input("enter a number (can be 0b, 0o, 0x or decimal): ")
base = int(input("enter a base to convert (2/8/10/16): "))
print("a number in base", base, "is:", convert(n, base))
if symmetric(convert(n, base)):
    print(convert(n, base), "is symmetric")
else:
    print(convert(n, base), "is not symmetric")
