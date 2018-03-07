def demo(*para):
    '''接收任意多个实数
    返回一个元组，第一个元素为所有参数的平均值，其他元素为所有参数中大于平均值得实数'''
    avg=sum(para)/len(para)
    g=[i for i in para if i > avg]
    return (avg,)+tuple(g)

print(demo(1,2,3,4))
