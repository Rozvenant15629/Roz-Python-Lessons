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
a = input("enter first number (can be 0b, 0o, 0x or decimal): ")
base1 = int(input("enter base to convert (2/8/10/16): "))
b = input("enter second number (can be 0b, 0o, 0x or decimal): ")
base2 = int(input("enter base to convert (2/8/10/16): "))
a_decimal = int(a, 0)
b_decimal = int(b, 0)
Sum = a_decimal + b_decimal
if a_decimal >= b_decimal:
    Difference = a_decimal - b_decimal
else:
    Difference = b_decimal - a_decimal
Product = a_decimal * b_decimal
print("Sum:", Sum)
print("Difference:", Difference)
print("Product:", Product)
print("first number in base", base1, "is:", convert(a, base1))
print("second number in base", base2, "is:", convert(b, base2))
