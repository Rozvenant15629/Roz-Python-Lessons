nums = input("enter a list: ")
numbers = list(map(int, nums.split(",")))
i = True
if len(numbers) < 2:
    i = False
    print("The list is less than 2")
else:
    ratio = numbers[1] / numbers[0]
    for a in range(1, len(numbers) - 1):
        if numbers[a + 1] / numbers[a] != ratio:
            i = False
            break
if i:
    print("The list is a geometric sequence")
else:
    print("The list isn't a geometric sequence")