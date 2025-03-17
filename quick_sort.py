# arr=list(map(int,input().split()))
# pivot=arr[0]
#
# while 1:
#     left=0
#     right=0
#     for i in range(1,8):
#         if arr[i]>pivot:
#             left=i
#             break
#     for j in range(7,0,-1):
#         if arr[j]<pivot:
#             right=j
#             break
#     if left>right:
#         arr[0],arr[right]=arr[right],arr[0]
#         break
#     arr[left],arr[right]=arr[right],arr[left]
#
# print(*arr)
arr=[4,1,7,9,6,3,3,6]

def quick(start,end):

    if start>=end: return
    pivot=start
    a=start+1
    b=end
    # pivot 위치 잡아주기
    while 1:
        while a<=end and arr[a]<=arr[pivot]:
            a+=1
        while b>=start and arr[b]>arr[pivot]:
            b-=1
        if a>b: break
        arr[a],arr[b]=arr[b],arr[a]
    arr[pivot], arr[b] = arr[b], arr[pivot]

    quick(start,b-1)
    quick(b+1,end)
quick(0,7)
print(arr)