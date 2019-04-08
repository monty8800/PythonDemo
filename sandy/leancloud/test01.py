__author__ = 'Monty'
__date__ = '2018/12/21 4:30 PM'

import leancloud,logging
from datetime import datetime

appId = '4nQemn4RcaJSTtvwcbddp4EX-gzGzoHsz'
appKey = 'o45OmvwAfI98vzR7jGizNYOJ'
masterKey = 'rYtsWLQ7u0LP9iJyzdmSGgKI'

leancloud.init(appId,appKey)
leancloud.use_region('CN')

logging.basicConfig(level=logging.DEBUG)

TestObject = leancloud.Object.extend('TestObject')
testObject = TestObject()
testObject.set('name','Monty')
testObject.set('work','ucforward')
testObject.save() # 增加一条数据

SupportedType = leancloud.Object.extend('SupportedType')
supported_type = SupportedType()
supported_type.set('string', '工作')
supported_type.set('int', 108)
supported_type.set('float', 1.890)
supported_type.set('boolean', True)
supported_type.set('list', [1, 2, [3, 4, 'string']])
supported_type.set(
    'dict', {'item1': 12, 'item2': 'string item', 'item3': [1, 2, '3']})
supported_type.set('date', datetime.now())
supported_type.save()









