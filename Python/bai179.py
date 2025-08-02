num = list(map(int, input("enter a string: ").split(",")))
diff = num[1] - num[0]
ari = True
for a in range(1, len(num) - 1):
    if num[a + 1] - num[a] != diff:
        ari = False
        break
if ari:
    print("YES")
else:
    print("NO")