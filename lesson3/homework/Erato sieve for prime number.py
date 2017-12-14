def Ereato(n):
    L = list(range(2,n))
    M=[]
    while True:
        N=[]
        M.append(L[0])
        for i in range(len(L)):
            if L[i]%L[0]==0:
                N.append(L[i])
        L = list(set(L).difference(set(N)))
        L.sort() #排序
        if len(L) == 0:break
    return(M)

    
