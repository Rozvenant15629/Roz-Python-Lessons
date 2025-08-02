n = input("enter a number (can be 0b, 0o, 0x or decimal): ")
i = int(n, 0)
bin_num = format(i, "b")
oct_num = format(i, "o")
dec_num = str(i)
hex_num = format(i, "X")
bases = {
    "Binary": bin_num,
    "Octal": oct_num,
    "Decimal": dec_num,
    "Hexadecimal": hex_num
}
count_ones = bin_num.count("1")
print("In all Bases")
for k, v in bases.items():
    print(f"{k} = {v}")
print("Number of '1' in binary:", count_ones)
fewest = min(bases, key = lambda x : len(bases[x]))
most = max(bases, key = lambda x: len(bases[x]))
print(f"fewest digits: {fewest} ({bases[fewest]})")
print(f"most digits: {most} ({bases[most]}))")