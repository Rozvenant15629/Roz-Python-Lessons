def digit(n):
    return len(str(n))
n = input("enter a number (can be 0b, 0o, 0x or decimal): ")
i = int(n, 0)
bin = format(i, "b")
oct = format(i, "o")
dec = str(i)
hex = format(i, "X")
print(f"Binary is: {bin} | Digits: {digit(bin)}")
print(f"Octal is: {oct} | Digits: {digit(oct)}")
print(f"Decimal is: {dec} | Digits: {digit(dec)}")
print(f"Hexadecimal is: {hex} | Digits: {digit(hex)}")
Bases = {
    "Binary": bin,
    "Octal": oct,
    "Decimal": dec,
    "Hexadecimal": hex
}
fewest = min(Bases, key=lambda x: len(Bases[x]))
largest = max(Bases, key=lambda x: len(Bases[x]))
print(f"System with fewest digits: {fewest} ({Bases[fewest]})")
print(f"System with largest digits: {largest} ({Bases[largest]})")