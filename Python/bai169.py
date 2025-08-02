def convert(n, base):
    i = int(n, 0)
    if base == 2:
        return format(i, "b")
    elif base == 8:
        return format(i, "o")
    elif base == 10:
        return str(i)
    elif base == 16:
        return format(i, "X")
    else:
        return "Base not supported!"
a = input("enter first number (can be 0b, 0o, 0x or decimal): ")
b = input("enter second number (can be 0b, 0o, 0x or decimal): ")
c = input("enter third number (can be 0b, 0o, 0x or decimal): ")
base1 = int(input("enter base to convert (2/8/10/16): "))
base2 = int(input("enter base to convert (2/8/10/16): "))
base3 = int(input("enter base to convert (2/8/10/16): "))
decimal_a = int(a, 0)
decimal_b = int(b, 0)
decimal_c = int(c, 0)
Sum = decimal_a + decimal_b + decimal_c
Difference = decimal_a - decimal_b - decimal_c
Product = decimal_a * decimal_b * decimal_c
Averange = (decimal_a + decimal_b + decimal_c) / 3
print("Sum:", Sum)
print("Difference:", Difference)
print("Product:", Product)
print("Averange:", round(Averange, 2))
print("Max:", max(decimal_a, decimal_b, decimal_c))
print("Min:", min(decimal_a, decimal_b, decimal_c))
print("first number in base", base1, "is:", convert(a, base1))
print("second number in base", base2, "is:", convert(b, base2))
print("third number in base", base3, "is:", convert(c, base3))