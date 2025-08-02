def convert(n, base):
    if base == 2:
        return format(n, "b")
    elif base == 8:
        return format(n, "o")
    elif base == 10:
        return str(n)
    elif base == 16:
        return format(n, "X")
    else:
        return "base doesn't support!"
a = int(input("enter first number: "))
b = int(input("enter second number: "))
base = int(input("enter base to convert (2/8/10/16): "))
print("first number in base", base, "is:", convert(a, base))
print("second number in base", base, "is:", convert(b, base))