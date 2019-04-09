from datetime import date
daysOfMonth=[31,28,31,30,31,30,31,31,30,31,30,31]

def myCalendar(year,month):
    #获取year年month月1日是周几
    start = date(year,month,1).timetuple().tm_wday#周一为1周日为6
    #打印头部信息
    print("{0}年{1}月日历".format(year,month).center(56))
    print('\t'.join(('日 一 二 三 四 五 六').split()))
    #获取该月有多少天，如果是2月并且是闰月，适当调整一下
    day = daysOfMonth[month-1]
    if month==2:
        if year%400==0 or (year%4==0 and year%100!=0):
            day+=1
    #生成数据，根据需要在前面填充空白
    result = [' '*8 for i in range(start+1)]#\t占7个空格
    result+=list(map(lambda d:str(d).ljust(8),range(1,day+1)))
    #print(result)
    #打印数据
    for i,day in enumerate(result):
        if i!=0 and i%7==0:
            print()
        print(day,end='')
    print()
def main(year,month=-1):
    if type(year)!=int or year<1000 or year>10000:
        print("Year error")
        return
    if type(month)==int:
        if month==-1:
            for m in range(1,13):
                myCalendar(year,m)
        elif month in range(1,13):
            myCalendar(year,month)
        else:
            print("Month error")
            return

main(2018,3)
    
