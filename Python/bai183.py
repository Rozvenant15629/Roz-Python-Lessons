def is_geometric_sequence(numbers):
    if len(numbers) < 2:
        return False
    else:
        ratio = numbers[1] / numbers[0]
        for i in range(1, len(numbers) - 1):
            if numbers[i + 1] / numbers[i] != ratio:
                return False
            break
    return True
nums = input("enter a list: ")
numbers = list(map(int, nums.split(",")))
if is_geometric_sequence(numbers):
    print("IS GEOMETRIC SEQUENCE")
else:
    print("IN NOT GEOMETRIc SEQUENCE")