arr=[6,4,1,4,7,8,1]
heap=[0]*20
hindex=1  # heap배열의 인덱스 역할

def insert(value):
    heap[hindex]=value #루트노드 저장
    now=hindex
    while 1:
        p=now//2 # 부모인덱스 구하기
        if p==0: break # 해당노드가 루트노드라면 그냥 off
        if heap[p] >= heap[now]: break # 부모가 크거나 같으면 끄기 (maxheap 구현중)
        heap[p],heap[now]=heap[now],heap[p] # 부모가 더 작으면 자식이랑 swap
        now=p # swap당한 부모가 그다음 프로세스의 자식이 되면서 위로 올라감...

def top():
    return heap[1]

def pop():
    heap[1]=heap[hindex]
    heap[hindex]=0
    now=1
    while 1:

        rson=now*2+1
        lson=now*2
        # 오른쪽 자식이 있는데 and 왼<오 앞으로 now(부모)랑 비교할 자식은 "오"
        if heap[rson]>=heap[lson]:
            son=rson
        else:
            son=lson
        # 자식이 없거나 or now(부모)가 자식보다 크다면 break
        if son>=hindex or heap[now]>heap[son]: break
        heap[now],heap[son]=heap[son],heap[now]
        now=son
# insert() 완전이진트리로 저장
# top() 루트노드를 리턴하는 함수
# pop() 루트노드 출력후 맨 뒤의 값을 맨 앞으로 올리고.. 자식들이랑 비교후 swap


for i in arr:
    insert(i)
    hindex+=1

for i in range(len(arr)):
    print(top(),end=' ')
    hindex-=1
    pop()