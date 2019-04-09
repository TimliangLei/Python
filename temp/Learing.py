weather = [("Monday","rainy"),("Tuesday","sunny"),("Wednesday","sunny"),
           ("Thursday","rainy"),("Friday","cloudy")]
formatter = "Weather of '{0[0]}' is '{0[1]}'".format
# for item in map(formatter,weather):
#     print(item)
for item in weather:
    print(formatter(item))

li = ["apple","peach","banana","pear"]
liStr = ','.join(li)
print(liStr)
print(liStr.split(','))
