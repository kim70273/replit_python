n = int(input()) #주어진 수 
d = [0]*30001 #최대 3만까지.
#d[1]은 0임.
for i in range(2,n+1):
  d[i] = d[i-1]+1 #1단계 더 필요하니.
  if i%2==0:
    d[i] = min(d[i],d[i//2]+1)
  if i%3==0:
    d[i] = min(d[i],d[i//3]+1)
  if i%5==0:
    d[i] = min(d[i],d[i//5]+1)
#/하면 실수가 나오므로 //로 연산해줘야됨.
print(d[n])
