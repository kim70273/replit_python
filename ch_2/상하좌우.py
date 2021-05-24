n = int(input())
plans = list(input().split())

x, y = 1, 1
m = ['R', 'L', 'D', 'U']
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in plans:
  for j in range(len(m)):
    if m[j]==i:
      nx = x+dx[j]
      ny = y+dy[j]
      if 0<nx<=n and 0<ny<=n:
        x=nx
        y=ny
        break
print(x, y)
