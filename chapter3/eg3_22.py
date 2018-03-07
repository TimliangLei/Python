import math

def IsPrime(n):
    m = int(math.sqrt(n))+1
    for i in range(2,m):
        if n%i == 0:
            return False
    return True

def demo(n):
    '''
        接收一个正偶数n
        输出两个素数，并且这两素数之和等于原来的正偶数
    '''
    if isinstance(n,int) and n>0 and n%2==0:
        for i in range(3,int(n/2)+1):
            #因为n为偶数，所以当i=2时候，n-i也要为偶数（肯定不是素数）
            if i%2==1 and IsPrime(i) and IsPrime(n-i):
                print(i,'+',n-i,'=',n)

demo(100) 
