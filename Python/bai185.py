lst = input("enter a list: ")
nums = list(map(int, lst.split(";")))
def is_valid_sequence(nums):
    if len(nums) < 2:
        return False
    else:
        for i in range(len(nums) - 1):
            if nums[i + 1] % nums[i] != 0:
                return False
    return True
if is_valid_sequence(nums):
    print("IS VALID SEQUENCE")
else:
    print("IS INVALID SEQUENCE")