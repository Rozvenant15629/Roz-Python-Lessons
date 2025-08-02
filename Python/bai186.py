def is_arithmetic_sequence(nums):
    if len(nums) < 2:
        return False
    else:
        diff = nums[1] - nums[0]
        for i in range(1, len(nums) + 1):
            if nums[i + 1] - nums[i] != diff:
                return False
            else:
                return True
lst = input("enter a list: ")
nums = list(map(int, lst.split(";")))
if is_arithmetic_sequence(nums):
    print("YES")
else:
    print("NO")