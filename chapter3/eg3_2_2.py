for n in range(100,1,-1):
    for i in range(2,n-1):
        if n%i==0:
            continue
        else:
            print(n)
            break
            
