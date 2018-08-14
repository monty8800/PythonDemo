# 1.获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now) # 2018-07-26 14:40:56.335224

print(type(now)) # <class 'datetime.datetime'>

# datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
#
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
#
# datetime.now()返回当前日期和时间，其类型是datetime。

# 2.获取指定日期和时间
dt = datetime(2018,7,26,14,42,0) # 用指定日期时间创建datetime
print(dt) # 2018-07-26 14:42:00

# 3.datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
print(dt.timestamp()) # 1532587320.0 - # 把datetime转换为timestamp

# 4.timestamp转换为datetime - fromtimestamp()转换
t = 1532587320.0
print(datetime.fromtimestamp(t)) # 2018-07-26 14:42:00 - 本地时间
print(datetime.utcfromtimestamp(t)) # 2018-07-26 06:42:00 - UTC时间

# 5.str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday) # 2015-06-01 18:19:59

# 6.datetime转换为str
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M')) # Thu, Jul 26 14:51

# 7.datetime加减 - 需要使用到timedelta
from datetime import datetime,timedelta
now = datetime(2018,7,26,14,42,0)
print(now) # 2018-07-26 14:54:19.088627
now += timedelta(hours=10) # 往后推10个小时
print(now) # 2018-07-27 00:55:04.780193
now += timedelta(days=2) # 往后推2天
print(now) # 2018-07-29 00:55:46.567957
now+=timedelta(days=3,hours=5) # 往后推3天5小时
print(now) # 2018-08-01 05:42:00

# 8.本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime(2018,7,26,14,42,0,tzinfo=tz_utc_8) # 强制加上时区
print(now) # 2018-07-26 14:42:00+08:00

# 9.时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 拿到UTC时间，并强制设置时区为UTC+0:00:
print(utc_dt) # 2018-07-26 07:01:15.906462+00:00

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) # astimezone()将转换时区为北京时间:
print(bj_dt) # 2018-07-26 15:02:19.795398+08:00
