nums = list(map(int, input("enter a string: ").split(",")))
if len(nums) < 2:
    print("You need at least 2 numbers!")
else:
    diff = nums[1] / nums[0]
    ratio = True
    for i in range(1, len(nums) - 1):
        if nums[i + 1] / nums[i] != diff:
            ratio = False
            break
    if ratio:
        print("YES")
    else:
        print("NO")