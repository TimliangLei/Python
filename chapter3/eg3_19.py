def demo(t):
    '''
        接收整数参数t
        返回斐波纳契数列大于t的第一个数
    '''
    a,b=1,1
    while b < t:
        a,b=b,a+b
    else:
        return b
print(demo(50))
