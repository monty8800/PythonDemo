__author__ = 'Monty'
__date__ = '2019/4/3 9:55 AM'


class ReportInfo(object):

    def __init__(self, id, reportType,reportId, houseCode, houseType, memberId, memberAreaCode, memberMobile, ownerId,
                 ownerAreaCode,ownerMobile, status, region, roomType, bedroomNum, bathroomNum, price, createTime,
                 requestedViewingTime, confirmedViewingTime):
        self.id = id
        self.reportType = reportType
        self.reportId = reportId
        self.houseCode = houseCode
        self.houseType = houseType
        self.memberId = memberId
        self.memberAreaCode = memberAreaCode
        self.memberMobile = memberMobile
        self.ownerId = ownerId
        self.ownerAreaCode = ownerAreaCode
        self.ownerMobile = ownerMobile
        self.status = status
        self.region = region
        self.roomType = roomType
        self.bedroomNum = bedroomNum
        self.bathroomNum = bathroomNum
        self.price = price
        self.creteTime = createTime
        self.requestedViewingTime = requestedViewingTime
        self.confirmedViewingTime = confirmedViewingTime

