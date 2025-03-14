# 5 7
# 0 1 3
# 0 3 9
# 0 4 5
# 1 2 7
# 1 4 1
# 2 3 1
# 4 2 1
# 0 3

import heapq
N,M=map(int,input().split()) # N,M  N=정점, M=횟수
arr=[[] for _ in range(N)]  # 각 시작점에서 도착점의 비용을 기록할 리스트

for i in range(M):
    a,b,cost=map(int,input().split()) # a=시작점 b=도착점 cost= 비용
    arr[a].append((b,cost)) # 각 시작점에 도착점과 비요을 튜플의 형태로 저장
start,end=map(int,input().split()) # 시작점과 도착점의 비용을 확인
result=[28e8]*N # 시작점에서 각 정점의 비용을 갱신할 리스트
result[start]=0
heap=[(0,start)] # 비용이 적을때 부터 뺴야하기 때문에 코스트를 먼저 저장
# heap=시작점에서 각 도착점에 비용이 최소일때 경유지로 설정하여 경유지를 거칠때 최소비용을 계산하기 위해 각 경유지와 비용을 저장할 heap
# 시작점이 경유지일때의 비용은 무조건 0
while heap: # heap가 비어질때까지
    n_cost,n=heapq.heappop(heap) # n_cost=현재 경유지를 거칠때의 비용 ,n=경유지
    if result[n]<n_cost: # 만약 경유지까지의 비용이 기존의 비용보다 크면 continue
        continue
    for end,end_cost in arr[n]:
        baro=result[end]
        new=n_cost+end_cost
        if new<baro:
            result[end]=new
            heapq.heappush(heap,(new,end))
print(*result)