#设置星期天的初始值为0
mondays=0
def getmonthdays(year):
    isleapyear=year%400==0 or (year%4==0 and (not year%100==0))
    if isleapyear:
        return [31,29,31,30,31,30,31,31,30,31,30,31]
    return [31,28,31,30,31,30,31,31,30,31,30,31]
#计算1899.12.31(这天是星期天）1901.1.1之间的天数
pastdays=1  #1899.12.31过一天是1900.1.1
monthdays=getmonthdays(1900)
for month in range (0,12):
    pastdays+=monthdays[month]
#计算1901.1.1到2000.12.31星期天的数字
for year in range(1901,2001):
    monthdays=getmonthdays(year)
    for month in range(0,12):
        if pastdays%7==0:
            mondays+=1
        pastdays+=monthdays[month]
print("1901年1月1月至2000年12月31日共有%d个星期天落在每月第一天"%mondays)