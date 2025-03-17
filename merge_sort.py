# arr=[2,3,5,7,1,2,5,9]
# start=0
# end=7
# mid=(start+end)//2
#
# a=start
# b=mid+1
#
# result=[]
#
# while 1:
#     if a>mid and b>end:
#         break
#     if a<=mid:
#         if arr[a]<=arr[b]:
#             result.append(arr[a])
#             a+=1
#
#     if b<=end:
#         if arr[a]>arr[b]:
#             result.append(arr[b])
#             b+=1
#         if a>mid:
#             for i in range(b,end+1):
#                 result.append(arr[i])
#                 b+=1
# print(*result)

arr=[2,7,5,3,1,5,9,2]

def merge(start,end):
    global arr
    mid=(start+end)//2
    if start==end:return # 같아지면 리턴
    merge(start,mid)
    merge(mid+1,end)
    a = start
    b = mid+1
    result = []
    # 자리 정렬
    while 1:
        if a > mid and b > end:
            break
        if a <= mid:
            if b > end or arr[a] <= arr[b]:  # arr[b]가 범위를 벗어나는 상황을 방지
                result.append(arr[a])
                a += 1
                continue  # 조건 충족 시 다음 반복으로 넘어감
        if b <= end:
            if a > mid or arr[a] > arr[b]:  # arr[a]가 범위를 벗어나는 상황을 방지
                result.append(arr[b])
                b += 1
                continue
    # 정렬된 값으로 배열을 변경
    for i in range(len(result)):
        arr[start+i] = result[i]

merge(0,7)

print(arr)
