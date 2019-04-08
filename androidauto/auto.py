__author__ = 'Monty'
__date__ = '2018/12/26 5:58 PM'

from uiautomator import device as d
from uiautomator import Device
d = Device('emulator-5556')
d.screen.on()
print(d.info)

# d(text="Chrome").click()
d(text="ACCEPT").click()


