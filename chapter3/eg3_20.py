import random

def MinAndIndex(lst):
    '''
        接收一个包含若干整数的列表
        返回一个元组，其中以的原数为列表lst中最小值
        其元素为最小值在lst中的下标
    '''
    m = min(lst);
    result = (m,)
    positions = [index+1 for index,value in enumerate(lst) if value == m]
    result = result + tuple(positions)
    return result

x = [random.randint(1,20) for i in range(50)]
print(x)
print(MinAndIndex(x))
