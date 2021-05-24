n, m = map(int, input().split())
#n개의 화폐 종휴, m원을 만들어야 됨.
money = [0]*n
for i in range(n):
  money[i] = int(input())

d=[10001]*(m+1)#0원부터 최대만원까지
d[0]=0

for i in money:
  for j in range(i,m+1):
    d[j] = min(d[j],d[j-i]+1)

if d[m]!=10001:
  print(d[m])
else:
  print(-1)

