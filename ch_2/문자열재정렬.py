n = input()

num=[]
s=[]

for i in range(len(n)):
  if ord('A')<=ord(n[i])<=ord('Z'):
    s.append(n[i])
  else:
    num.append(int(n[i]))

num.sort()
s.sort()

print(s+num)