#%%
! time ./01.py < sample.in > sample.out

#%%
with open("color/sample02.in", "r") as f:
    S, C, K = list(map(int, f.readline().split()))
    D = list(map(int, f.readline().split()))

def color(S, C, K, D):
    # edge cases
    if C == 0:
        m=0 # Machine capacity cannot be zero!
    elif (S<1) or (len(D)<1):
        m=0 # No socks to wash!
    else:
        # sort D
        D.sort()
        # init
        min, m, c = D[0], 1, 1
        for i in D[1:]:
            if abs(i-min) > K:
                m, c, min = m+1, 1, i
            else: c+=1
            if c==C:
                m, c = m+1, 0
    return m

print(color(S, C, K, D))
