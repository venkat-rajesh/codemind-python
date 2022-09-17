n=int(input())
s=1
p=0
while n>0:
    b=n%10
    s*=b
    p+=b
    n=n//10
print(s-p)