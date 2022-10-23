t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    v=n/a
    s=n/b
    g=v+s
    if g>=k:
        print("Win")
    else:
        print("Lose")