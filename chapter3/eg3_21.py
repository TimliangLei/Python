def Yanghui_Triangle(t):
    '''
        接收一个t整数
        打印一个杨辉三角
    '''
    result  = [[1],[1,1]]
    line = [1,1]
    for i in range(2,t):
        r=[]
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])
        line=[1]+r+[1]
        result.append(line)
    return result
def output(result):
    for item in result:
        print(item)

output(Yanghui_Triangle(10))
