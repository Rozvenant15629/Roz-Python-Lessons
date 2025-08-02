def is_fibonacci(nums):
    if len(nums) < 3:
        return False
    else:
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] != nums[i + 2]:
                return False
    return True
lst = input("enter a list: ")
nums = list(map(int, lst.split(";")))
if is_fibonacci(nums):
    print("YES")
else:
    print("NO")