
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,M=map(int,input().split())
    B_lst=[list(map(str,input().strip())) for _ in range(N)]
    new_lst=[[] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if B_lst[i][j]=='0':
                new_lst[i]+='0'
            elif B_lst[i][j]!='0':
                a=bin(int(B_lst[i][j],16))[2::]
                new_lst[i]+=a


    def numberss(st):

        if st==[2,1,1]:
            return 0
        elif st==[2,3,1]:
            return 5
        elif st==[2,2,1]:
            return 1
        elif st==[1,1,4]:
            return 6
        elif st==[1,2,2]:
            return 2
        elif st==[3,1,2]:
            return 7
        elif st==[4,1,1]:
            return 3
        elif st==[2,1,3]:
            return 8
        elif st==[1,3,2]:
            return 4
        elif st==[1,1,2]:
            return  9

    def cal1(st):
        num=[]
        count=0
        lst_st = list(st)
        start = int(lst_st[0])
        for i in range(0,len(lst_st)):
            if start!=int(lst_st[i]):
                if start==0:
                    start=1
                    num.append(count)
                    count = 1
                elif start==1:
                    start=0
                    num.append(count)
                    count = 1
            else:
                count+=1
            if i == (len(lst_st)-1):
                num.append(count)
        Min=min(num)

        for i in range(len(num)):
            num[i]=num[i]//Min
        num.pop(0)
        return num



    def cal2(st):
        num = []
        count = 0
        lst_st = list(st)
        start=int(lst_st[0])
        for i in range(0, len(lst_st)):
            if start != int(lst_st[i]):
                if start == 0:
                    start = 1
                    num.append(count)
                    count = 1
                elif start == 1:
                    start = 0
                    num.append(count)
                    count = 1
            else:
                count += 1
            if i == (len(lst_st) - 1):
                num.append(count)
        Min = min(num)

        for i in range(len(num)):
            num[i] = num[i] // Min
        num.pop(0)
        return num
    def step4(st,idx):
        if (idx)%2==1:
            ret_lst1=cal1(st)
            return ret_lst1
        elif (idx)%2==0:
            ret_list2=cal2(st)
            return ret_list2

    def Check(lst):
        if not lst:
            return
        else:
            lst=lst[::-1]
            # 각 그룹의 갯수
            t=len(lst)//7
            idx=0
            ones=0
            twos=0
            for i in range(0,len(lst),t):
                st=''
                print(st)
                idx+=1
                for j in range(i,i+t):
                    st+=lst[j]
                st=st[::-1]
                ret=step4(st,idx)
                print(st)

                if (i+1)%2!=0:
                    result=numberss(ret)
                    ones+=result
                elif (i+1)%2==0:
                    result=numberss(ret)
                    twos+=result
            check=ones*3+twos
            if check%10==0:
                return ones+twos

    def Cal(lst):
        dap=[]
        while lst[-1]=='0':
            lst.pop()
            if not lst:
                break
        ret=Check(lst)
        if dap:
            dap.append(ret)
        return dap

    for i in new_lst:
        ret=Cal(i)
        print(ret)
    print(new_lst)

    # ///////////////////////////////////////////////////////////////////////////////////
