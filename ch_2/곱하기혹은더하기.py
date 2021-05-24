data = input()

n=data[0]
for i in range(1,len(data)):
    if int(data[i])<=1 or n<=1:
        n+=data[i]
    else:
        n*=data[i]

print(n)