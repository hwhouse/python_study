# 递归求斐波那契数列的第n项
def fib(n):
    if n==1:
        return(1)
    if n==2:
        return(1)
    return(fib(n-1)+fib(n-2))

def fiblist(n):
    L = []
    for i in range(1,n+1):
        L.append(fib(i))
    
    return(L)

