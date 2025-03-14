# 각각의 독립된 data를 그룹화 시켜 관리하고자 할 때 사용하는 자료구조
k=int(input()) # 정점수
N=int(input()) # 간선 정보 수
lst=[list(map(str,input().split())) for _ in range(N)] # 간선 리스트화
cnt=0 # 간선 수
cost=0 # 간선 비용
lst.sort(key=lambda x:int(x[2])) #재정렬
arr=[0]*200 # 간선별로 이어져있는 최종 정점을 입력하기 위한 배열
print(lst)

def find(m): # 주어진 정점과 이어져있는 최상위 점저을 구하기 위한 함수
    global arr
    if arr[ord(m)]==0: # 정점에 입력되어 있는 값이 0 이라면 그 정점이 최상위 정점
        return m
    ret=find(arr[ord(m)]) # 0이 아닌 다른 값이 입력되어 있다면 다시 들어가 그 최상위 점정을 찾기위한 재귀
    arr[ord(m)]=ret # 주어진 정점을 최상위 정점으로 바꾸어줌으로써 반복회수 최소화
    return ret

def union(a,b,ind): # 정점끼리 연결시키기 위한 함수
    global arr,cnt,cost
    BossA,BossB=find(a),find(b) # 입력 받은 각각의 정점의 최상위 정점 구하기
    if BossA==BossB: # 만약 최상위 정점이 서로 같다면 이미 이어져있으므로 아무것도 안하고 종료
        return
    cnt+=1 # 그게 아니라면 간선수 증가 연결
    cost+=int(lst[ind][2]) # 비용 증가
    arr[ord(BossB)]=BossA # 간선 연결

for i in range(N):
    if cnt==k-1:
        print(cnt,cost)
        break
    union(lst[i][0],lst[i][1],i)

# 5
# 8
# A B 9
# A C 3
# A E 7
# B C 14
# B D 11
# C D 1
# C E 5
# A D 20