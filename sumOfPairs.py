def get_sum(a,n,k):
    a.sort()
    i,j=0,n-1

    while(i<j):
        sum=a[i]+a[j]
        if sum==k:
            return True 
        elif sum<k:
            i+=1
        else:
            j-=1 
    return False 





t=int(input())
for i in range(t):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    get_sum(a,n,k)
    print(get_sum(a,n,k))
