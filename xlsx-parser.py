from openpyxl import load_workbook

wb = load_workbook('')

sheet = wb.get_sheet_by_name('')

import peewee
from peewee import *

db = MySQLDatabase('test', user='root', password='root', host='localhost', port=3316)
Data1 = Table('table1', ('id', 'name'))
Data1 = Data1.bind(db)

maxCountRow = sheet.max_row

for i in range(2, maxCountRow):
    value = sheet['C' + str(i)].value
    Data1.insert(name=value).execute()
