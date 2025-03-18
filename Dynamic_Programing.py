# 비트 연산 코드
N,K=map(int,input().split())
lst=[]
Max=0
for i in range(N):
    W,V=map(int,input().split())
    lst.append((W,V))
for i in range(1<<N):
    value=0
    weigh=0
    for j in range(N):
        if i&(1<<j):
            weigh+=lst[j][0]
            value+=lst[j][1]
            if weigh>K:
                break
    else:
        if value>Max:
            Max=value
print(Max)

# # DP 비교 갱신 강사님!!!!!!
n,k=map(int,input().split())
knapsack=[[0 for _ in range(k+1)] for _ in range(n+1)]
item=[[0,0]]
for i in range(1,n+1):
    item.append(list(map(int,input().split())))
# 배열에 값 채워 넣기
for i in range(1,n+1): # 물건종류
    for j in range(1,k+1): # 가방무게
        weight=item[i][0]
        value=item[i][1]

        if j<weight: # 물건무게 > 여유있음가방무게
            knapsack[i][j]=knapsack[i-1][j] # 그전 단계에서 구했던 값으로 갱신
        else: # 가방에 물건을 넣을 수 있는경우
            knapsack[i][j]=max(knapsack[i-1][j], value+knapsack[i-1][j-weight])
            # 그전 단계에서 구했던 최대효율 vs 지금물건 1개 넣은것 + 남은 무게 (그전단계에서 구한)

print(knapsack[n][k])

# # 동전 거스름 돈
N,K=map(int,input().split())
Dong_lst=[0]
for i in range(N):
    a=int(input())
    Dong_lst.append(a)
knapsack=[[100 for _ in range(K+1)] for _ in range(N+1)]
Dong_lst.sort()
for i in range(1,N+1): # 동전 경유
    for j in range(1,K+1): # 금액
        coin=Dong_lst[i]
        value=j//coin
        merge=j%coin
        if merge==0: # 딱 나누어 떨어지면 몫
            knapsack[i][j]=value
        else: # 나누어 떨어지지 않을때
            if value==0: # 몫이 0이라면
                knapsack[i][j]=knapsack[i-1][j] # 윗줄값 갱신
            else: # 몫이 0이 아니라면
                new_money = merge # 나머지 구하고
                knapsack[i][j]=min(value+knapsack[i][new_money],knapsack[i-1][j])  # 남은 금액과 몫의 합과 위의 값과 비교
print(knapsack[N][K])

# LCS 최장 공통 부분 문자열 Longest Common Substring
# LCS 최장 공통 부분 수열 Longest Common Subsequence
# LIS 최장 증가 부분 수열 Longest Increasing Subsequence

# LCS 최장 공통 부분 문자열
def lcs(s1,s2):

    len1,len2=len(s1),len(s2)

    arr=[[0]*(len2+1) for _ in range(len1+1)]
    Max=0
    idx=0
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1]==s2[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
                Max=max(Max,arr[i][j])
            else:
                arr[i][j]=0
    return Max
s1=input()
s2=input()
print(lcs(s1,s2))


# 민코딩 29.5-9
def lcs(s1,s2):

    len1,len2=len(s1),len(s2)

    arr=[[0]*(len2+1) for _ in range(len1+1)]
    Max=0
    idx=0
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1]==s2[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
                if arr[i][j]>Max:
                    Max=arr[i][j]
                    idx=i
            else:
                arr[i][j]=0
    string=s1[idx-Max:idx]
    return string
s1=input()
s2=input()
print(lcs(s1,s2))

# 최장 공통 부분 수열
def lcs(s1,s2):
    len1,len2=len(s1),len(s2)
    arr=[[0]*(len2+1) for _ in range(len1+1)]

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1]==s2[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    return arr[len1][len2]

s1="BABJYP"
s2="ABPABY"
print(lcs(s1,s2))

# LIS 최장 증가 부분 수열
N=int(input())
arr=list(map(int,input().split()))
result=[1]*N
for y in range(N): # 기준이 되는곳
    std=arr[y] # 기준 값
    for x in range(y): # 비교대상
        value=arr[x] # 비교대상
        if std>value: # 기준이 되는 값>비교대상
            result[y]=max(result[x]+1,result[y]) # 원래 값이랑 비교가 되는 값의 +1 과 비교하여 큰 값 저장

print(max(result))