while True:
    try:
        a=input()
    except:
        break
   
    n=len(a)
    if 0==n:
        break
    b=[]
    c=[]
    for i in range(n):
        b.append(ord(a[i])-97)
        c.append(0)
    for i in range(n-1):
        b.append(ord(a[i])-97)
        c.append(0)
    
    for i in range(n):
        for j in range(i,-1,-1):
            c[j]=c[j]*26+b[i]
    for i in range(n,2*n-1):
        for j in range(i,i-n,-1):
            c[j]=c[j]*26+b[i]
    
    ans=(26**n)-1
    for i in range(n):
        if ans>c[i]:
            ans=c[i]
    
    out=''
    for _ in range(n):
        out=chr(97+ans%26)+out
        ans //=26
    print(out)
    '''
    for rst in c:
        for _ in range(n):
            print(rst%26,end=' ')
            rst //=26
        print()
    '''