import sys
input = sys.stdin.readline
INF = int(1e9)#무한을 의미하는 값으로 10억 설정

#노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
#출발 노드 값 입력
start = int(input())
#각 노드에 연결 되어있는 노드 정보 담는 배열
graph = [[] for i in range(n+1)]
#방문을 체크하는 배열
visited = [False]*(n+1)
#최단거리 테이블 우선 전부 무한대로 초기화
distance = [INF]*(n+1)

#모든 간선의 정보 입렵 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  #a노드에서 b노드로 가는 비용이 c
  graph[a].append((b,c))

#방문하지 않은 노드중 가장 거리가 짧은 노드 번호 반환
def get_smallest_node():
  minvalue = INF
  index = 0 #가장 거리가 짧은 노드(인덱스)
  for i in range(1,n+1):
    if distance[i]<minvalue and not visited[i]:
      minvalue = distance[i]
      index = i
  return index

#다익스트라알고리즘
def dijkstra(start):
  #시작노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True

  for j in graph[start]:
    distance[j[0]] = j[1]

  #시작 노드를 제외한 n-1개의 노드에 대해서 반복
  for i in range(n-1):
    #현재 노드중 가장 짧은 거리노드를 꺼내서 방문처리
    now = get_smallest_node()
    visited[now] = True
    #현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
      cost = distance[now]+j[1]
      #현재 노드를 거쳐서 다른 노드로 가는 거리가 더 짧은 경우
      if cost<distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)#다익스트라 알고리즘 실행

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
  if distance[i]==INF:
    print('INF')#도달할 수 없는 경우
  else:
    print(distance[i])
