array = list(map(int,input().split()))
array.sort()

result = 0
count = 0
for i in range(len(array)):
  count+=1
  if array[i]<=count:
    count=0
    result+=1

print(result)