from django.db import models
from datetime import datetime


# Create your models here.
class Luhuo(models.Model):
    add_time = models.DateField(default=datetime.now, verbose_name='下单日期')
    platform = models.CharField(max_length=2,
                                choices=(('tb', '淘宝'), ('tm', '天猫'), ('mn', '猫宁'), ('sn', '苏宁'), ('jd', '京东')),
                                verbose_name='下单平台')
    order_num = models.CharField(max_length=50, unique=True, verbose_name='订单号')
    product = models.CharField(max_length=100, verbose_name='产品名称')
    num = models.IntegerField(verbose_name='数量')
    price = models.FloatField(verbose_name='价格')
    money = models.FloatField(default=0.0, verbose_name='金额')
    gather = models.FloatField(default=0.0, verbose_name='收款')

    class Meta:
        verbose_name = "撸货订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product + '-' + self.order_num
