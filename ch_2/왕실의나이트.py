n = input()

dx = [-1,1,-1,1,2,2,-2,-2]
dy = [2,2,-2,-2,-1,1,-1,1]

x=int(n[1])
y=ord(n[0])-ord('a')+1

count=0

for i in range(len(dx)):
  nx = x+dx[i]
  ny = y+dy[i]
  if 0<nx<=8 and 0<ny<=8:
    count+=1
print(count)
