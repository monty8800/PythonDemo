__author__ = 'Monty'
__date__ = '2019/2/15 7:43 PM'

import json as js


with open("event.json",'r') as load_f:
    load_dict = js.load(load_f)

map_obj = load_dict['events']
for i in map_obj:
    # print(i['name'])
    print(i['token'])

