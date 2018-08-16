import xml.etree.ElementTree as et
import csv

tree = et.parse('./file/strings.xml')
root = tree.getroot()

strings = [['字段名', '值']]

for child in root:
    # print(child.attrib['name'], child.text)
    c = [child.attrib['name'], child.text]
    print(c)
    strings.append(c)

with open('./file/strings.csv', 'w', newline='', encoding='utf_8_sig') as f:
    csv_f = csv.writer(f, dialect="excel")
    for s in strings:
        csv_f.writerow(s)
