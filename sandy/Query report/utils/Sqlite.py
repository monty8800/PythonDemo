__author__ = 'Monty'
__date__ = '2019/4/3 9:28 AM'
import sqlite3
from .ReportInfo import ReportInfo


def createTable():
    conn = sqlite3.connect('./report/report.db')
    print('Opened database successfully')
    c = conn.cursor()
    c.execute('CREATE TABLE REPORT_INFO('
              'ID INT PRIMARY KEY AUTOINCREMENT NOT NULL ,'
              'REPORT_TYPE INT NOT NULL ,'
              'REPORT_ID TEXT NOT NULL ,'
              'HOUSE_CODE TEXT NOT NULL ,'
              'HOUSE_TYPE TEXT NOT NULL,'
              'MEMBER_ID TEXT NOT NULL,'
              'MEMBER_AREA_CODE TEXT NOT NULL,'
              'MEMBER_MOBILE TEXT NOT NULL,'
              'OWNER_ID TEXT NOT NULL,'
              'OWNERAREA_CODE TEXT NOT NULL,'
              'OWNER_MOBILE TEXT NOT NULL,'
              'STATUS TEXT NOT NULL,'
              'REGION TEXT NOT NULL,'
              'ROOM_TYPE TEXT NOT NULL,'
              'BEDROOM_NUM TEXT NOT NULL,'
              'BATHROOM_NUM TEXT NOT NULL,'
              'PRICE DOUBLE NOT NULL,'
              'CREATE_TIME TEXT NOT NULL,'
              'REQUESTED_VIEWING_TIME TEXT NOT NULL,'
              'CONFIRMED_VIEWING_TIME TEXT NOT NULL)')

    c.close()
    conn.commit()
    conn.close()


def insert(report):
    # sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
    #        LAST_NAME, AGE, SEX, INCOME) \
    #        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
    #       ('Mac', 'Mohan', 20, 'M', 2000)
    report = ReportInfo(report)
    conn = sqlite3.connect('./report/report.db')
    print('Opened database successfully')
    c = conn.cursor()
    c.execute(
        "INSERT INTO REPORT_INFO VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        report.reportType, report.reportId, report.houseCode, report.houseType, report.memberId, report.memberAreaCode,
        report.memberMobile, report.ownerId, report.ownerAreaCode, report.ownerMobile, report.status, report.region,
        report.roomType, report.bedroomNum, report.bathroomNum, report.price, report.creteTime,
        report.requestedViewingTime, report.confirmedViewingTime))

    c.close()
    conn.commit()
    conn.close()


createTable()
