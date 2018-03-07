from math import pi as PI
def CircleArea(r):
    if isinstance(r,(int,float)):
        return PI* r * r
    else:
        print('You must give me an integer or float as radius.')
print(CircleArea(3))
