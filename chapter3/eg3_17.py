import time
def demo_eg3_17(s):
    '''接收字符串
        返回一个元组:
            第一个元素为大写字母的个数
            第二个元素为小写字母的个数'''
    result=[0,0]
    for ch in s:
        if 'a'<=ch<='z':
            result[1]+=1
        elif 'A'<=ch<='Z':
            result[0]+=1
    return result

def my_eg3_17(s):
    '''接收字符串
        返回一个元组:
            第一个元素为大写字母的个数
            第二个元素为小写字母的个数'''
    result=[0,0]
    for ch in s:
        if ch.islower():
            result[1]+=1
        elif ch.isupper():
            result[0]+=1
    return result

start=time.time()
print(demo_eg3_17('aaaAAAbbBBadccdfaf'))
print("demo_eg3_17 time:{0}".format(time.time()-start))
start=time.time()
print(my_eg3_17('aaaAAAbbBBadccdfaf'))
print("my_eg3_17 time:{0}".format(time.time()-start))
