#课堂改正
lim = 5
def fib(a,b,lev = 1):
    if lev == lim:return(a+b)
    return(fib(b,a+b,lev = lev+1))
fib(1,1)
