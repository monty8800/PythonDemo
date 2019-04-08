__author__ = 'Monty'
__date__ = '2019/4/2 3:43 PM'
import paramiko
import operator

ip = '47.91.110.186'
username = 'root'
password = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(ip, 22, username, password)

cmd = 'sh /opt/exprot.sh'

stdin, stdout, stderr = ssh.exec_command(cmd)  # 执行命令

reportInfoList = []
for line in stdout:
    reportInfoList.append(line)
    print(line)

try:
    transport = paramiko.Transport((ip, 22))
    transport.connect(username=username, password=password)
except Exception as e:
    print(e)

sftp = paramiko.SFTPClient.from_transport(transport)  # 通过sftp连接服务器

dirs = sftp.listdir_attr("/opt")  # 通过sftp列出/opt目录下的所有文件

dirs.sort(key=operator.attrgetter('st_mtime'))  # 按照创建时间进行排序

print('-------------------------')
f = dirs[len(dirs) - 1]  # 取最新的一个文件作为要下载的文件
print(f)

sftp.get('/opt/' + f.filename, './report/' + f.filename)

sftp.close()
ssh.close()

reservationCount = 0  # 议价总数
appointmentCount = 0  # 预约总数
reservationSuccessfully = 0  # 议价成功数量
appointmentSuccessfully = 0  # 预约成功数量
reservationLastId = 0  # 最后一条议价记录ID
appointmentLastId = 0  # 最后一条预约记录ID
registerCount = 0

for info in reportInfoList:
    if ('AppointmentData' in info):
        appointmentCount += 1
        if ('status=\'4\'' in info):
            appointmentSuccessfully += 1
    elif ('ReservationData' in info):
        reservationCount += 1
        if ('status=\'1\'' in info):
            reservationSuccessfully += 1
    elif ('注册用户数：' in info):
        registerCount = info[info.index('：') + 1:]
        registerCount = int(registerCount.strip())

appointmentData = []
reservationData = []
for i in reportInfoList:
    if ('AppointmentData' in i):
        appointmentData.append(i)
    elif ('ReservationData' in i):
        reservationData.append(i)

app = appointmentData[len(appointmentData) - 1]
res = reservationData[len(reservationData) - 1]
appointmentLastId = app[app.index('=') + 2:app.index(',') - 1]
reservationLastId = res[res.index('=') + 2:res.index(',') - 1]

import time
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
theDayBeforeYesterday = yesterday - datetime.timedelta(days=1)
period = time.strftime('%p', time.localtime())
createTime = time.strftime('%H:%M:%S', time.localtime())

if (period == 'AM'):
    print('------------Yesterday--------------')
    print('迪拜时间:%s 0:00~%s 8:00 数据统计' % (yesterday, today))
else:
    print('迪拜时间:%s 8:00~12:00 数据统计' % (today))

print('议价总数:%s,成功:%s' % (reservationCount, reservationSuccessfully))
print('预约总数:%s,成功:%s' % (appointmentCount, appointmentSuccessfully))

# print('-------------------------')
# print('最后一条议价信息的ID:' + reservationLastId)
# print('最后一条预约信息的ID:' + appointmentLastId)
print('-------------------------')
if (appointmentCount > 0):
    print('*有预约成功，请注意!!!')
if (reservationSuccessfully > 0):
    print('*有议价成功，请注意!!!')

import sqlite3

conn = sqlite3.connect('./report/report.db')
cursor = conn.cursor()
yesterdayResult = cursor.execute('SELECT * FROM STATISTICS WHERE STATISTICS_DATETIME = ?', (yesterday,))
yesterdayResultList = yesterdayResult.fetchall()

theDayBeforeYesterdayResult = cursor.execute('SELECT * FROM STATISTICS WHERE STATISTICS_DATETIME = ?',
                                             (theDayBeforeYesterday,))
theDayBeforeYesterdayList = theDayBeforeYesterdayResult.fetchall()

todayPmResult = cursor.execute('SELECT * FROM STATISTICS WHERE STATISTICS_DATETIME = ? AND PERIOD = ?', (today, 'AM'))
todayPmResultList = todayPmResult.fetchall()

yesterdayRegisterCount = yesterdayResultList[len(yesterdayResultList) - 1][6]
theDayBeforeYesterdayRegisterCount = theDayBeforeYesterdayList[len(theDayBeforeYesterdayList) - 1][6]

result = cursor.execute('SELECT * FROM STATISTICS WHERE (STATISTICS_DATETIME = ? AND PERIOD = ?)', (today, period))
statisticsList = result.fetchall()

# if (len(statisticsList) <= 0):
sql = 'INSERT INTO STATISTICS (STATISTICS_DATETIME,PERIOD,RESERVATION_COUNT,APPOINTMENT_COUNT,RESERVATIONSUCCESSFULLY,APPOINTMENTSUCCESSFULLY,APPOINTMENT_LAST_ID,RESERVATION_LAST_ID,"TIME",REGISTER_COUNT) VALUES (?,?,?,?,?,?,?,?,?,?)'
cursor.execute(sql, (
today, period, reservationCount, appointmentCount, reservationSuccessfully, appointmentSuccessfully, appointmentLastId,
reservationLastId, createTime, registerCount))
# else:
#     print('--------------更新数据')
#     sql = 'UPDATE STATISTICS SET RESERVATION_COUNT =?,APPOINTMENT_COUNT=?,RESERVATIONSUCCESSFULLY=?,APPOINTMENTSUCCESSFULLY=?,APPOINTMENT_LAST_ID=?,RESERVATION_LAST_ID=?,TIME=? WHERE (STATISTICS_DATETIME = ? AND PERIOD = ?)'
#     cursor.execute(sql,( reservationCount, appointmentCount, reservationSuccessfully, appointmentSuccessfully,appointmentLastId,reservationLastId,time, today, period))

cursor.close()
conn.commit()
conn.close()


if (period == 'AM'):
    print('与%s  0:00~%s 12:00 数据统计对比：' % (str(today - datetime.timedelta(days=3)), str(today - datetime.timedelta(days=2))))
    yesterdayAppointmentLast = yesterdayResultList[len(yesterdayResultList) - 1][7]
    yesterdayReservationLast = yesterdayResultList[len(yesterdayResultList) - 1][8]
    print('议价总数新增：%s' % (appointmentLastId - yesterdayAppointmentLast))
    print('预约总数新增：%s' % (reservationLastId - yesterdayReservationLast))
else:
    print('------------Today AM--------------')
    print('%s 8:00与12:00 数据统计对比：' % today)
    todayAppointmentLast = todayPmResultList[len(todayPmResultList) - 1][7]
    todayReservationLast = todayPmResultList[len(todayPmResultList) - 1][8]
    todayAppointmentSuccessfully = todayPmResultList[len(todayPmResultList) - 1][4]
    todayReservationSuccessfully = todayPmResultList[len(todayPmResultList) - 1][5]
    print('预约总数新增：%s' % (int(appointmentLastId) - todayAppointmentLast))
    print('议价总数数新增：%s' % (int(reservationLastId) - todayReservationLast))
    print('预约成功总数新增：%s' % (int(appointmentSuccessfully) - todayAppointmentSuccessfully))
    print('议价成功总数新增：%s' % (int(reservationSuccessfully) - todayReservationSuccessfully))

print('--------------------------')
print('截止%s 北京时间12 :00，迪拜时间：8:00 注册用户数： %d人  比昨日增长%d人 比两天前增长%d人' % (
today, registerCount, registerCount - yesterdayRegisterCount, registerCount - theDayBeforeYesterdayRegisterCount))
print('--------------------------')
