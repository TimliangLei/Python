import time
def demo(lst,k):
    x = lst[:k]
    x.reverse()
    y=lst[k:]
    y.reverse()
    r=x+y
    return list(reversed(r))

def demo1(lst,k):
    x = lst[:k]
    y=lst[k:]
    r=y+x
    return list(r)
def demo2(lst,k):
    return lst[k:]+lst[:k]
lst = list(range(1,21))
print(lst)
start=time.time()
print(demo(lst,5))
print("demo time:{0}".format(time.time()-start))
start=time.time()
print(demo1(lst,5))
print("demo1 time:{0}".format(time.time()-start))
start=time.time()
print(demo2(lst,5))
print("demo2 time:{0}".format(time.time()-start))
