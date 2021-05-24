fList = [1, 3, 1, 5]
a = [0] * 100
a[0] = fList[0]
a[1] = max(fList[0], fList[1])

for i in range(2, len(fList)):
    a[i] = max(a[i - 1], a[i - 2] + fList[i])
print(a)
