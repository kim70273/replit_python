import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)#무한을 의미하는 값으로 10억 설정

#노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]#1~n까지 담을 공간
distance = [INF]*(n+1)

#모든 간선의 정보 입력 받기
for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))#b로 가는데 c만큼 비용.

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  #우선 순위 큐에 넣는 것은 heappush
  #빼는 것은 heappop
  distance[start]=0

  while q:#큐가 다 비어질때까지 반복
    dist, now = heapq.heappop(q)

    if distance[now]<dist:
      continue
    
    for i in graph[now]:
      cost = dist+i[1]
      if distance[i[0]]>cost:
        distance[i[0]]=cost
        heapq.heappush(q,(cost, i[0]))

dijkstra(1)
count =0
max = 0
for i in distance:
  if i!=INF:
    count+=1
    if i>max:
      max=i
  
print(count, max)

#우선순위 큐를 이용한 다익스트라 알고리즘




