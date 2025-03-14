# 위상정렬 -> 수행되어야 할걸 다 수행시키고 뽑기위해 먼저해야할걸 도출하는 알고리즘
# step1: 인접행렬 또는 인접리스트로 변환
# step2: 사전 작업의 개수를 확인하는 리스트 생성
# step3: 작업 수행여부를 확인할 used배열 생성
# step4: 바로 작업을 할 수 있는 인덱스를 큐에 대입
# step5: 작업을 할 인덱스를 큐에서 제거하면서 확인 후 사전작업 리스트 used 수정
from collections import deque

N, M = map(int, input().split())
count = [0] * N
used = [0] * N
arr = [[] for _ in range(N)]  # 인접 리스트로 변경

for i in range(M):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)

for i in range(N):
    for j in arr[i]:  # 인접 리스트 사용
        count[j] += 1

q = deque()
for i in range(N):
    if count[i] == 0:
        q.append(i)
        used[i] = 1
while q:
    ret=q.popleft()
    print(ret+1,end=' ')
    for i in arr[ret]:
        if count[i]==1:
            if used[i] == 0:
                count[i]=0
                used[i]=1
                q.append(i)
        else:
            count[i]-=1