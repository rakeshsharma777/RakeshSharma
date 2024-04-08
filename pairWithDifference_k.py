def pair_with_diff_k(a,k):
    num_set=set(a)
    for nu in a:
        if nu-k in num_set and nu-k!=nu:
            return True 
    return False

t=int(raw_input().strip())
for i in range(t):
    n,k=map(int,raw_input().strip().split())
    a=map(int,raw_input().strip().split())
    res=pair_with_diff_k(a,k)
    if res==True:
        print("true")
    else:
        print("false")
