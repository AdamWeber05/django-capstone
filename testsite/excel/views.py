from django.shortcuts import render
from django.views.generic.base import TemplateView


# @param: TemplateView -> Django generic Template to render html
# Returns excel_home.html that will render when this view is accessed
class ExcelPageView(TemplateView):
    template_name="excel_home.html"

import xlwt
import datetime

from django.http import HttpResponse
from solookup.models import Boat


# Funciton that returns the excel document with production floor information about all the boats
# @param: request -> type of request (GET, POST, etc)
def export_boat(request):
    # Set up fo the attachment to download
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Production_Floor.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Production Floor') #this will make a sheet named Production Floor

    # iterator
    row_num = 0

    # All columns to be added to Document
    columns = ['S/O', 'Dealer', 'Model', 'Motor', 'Start Date', 'Color', 'Prep', 'Gel', 'Skin', 'Bulk', 'Floor', 'Box', 'Pull', 'Grind', 'Cut', 'Patch', 'Hardware', 'Cap', 'Foam', 'Con', 'MTR', 'Rig', 'Uph', 'C/C', 'Insp', 'Shipped']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], style = xlwt.easyxf('pattern: pattern solid, fore_colour white; font: bold True; borders: left thin, right thin, top thin, bottom thin')) # at 0 row 0 column

    # Sheet body, remaining rows

    # Each row is its own boat object, days are colored depending on what day it is
    rows = Boat.objects.all().values_list('so_num', 'dealer_name', 'model', 'motor', 'anticipated_Start', 'color', 'prep', 'gel', 'skin','bulk','floor','box','pull','grind','cut','patch','hw','cap','foam','con','mtr','rig','uph','cc','insp','ship')
    for row in rows:
        row_num += 1
        for col_num in range(6):
            if isinstance(row[col_num], datetime.date):
                ws.write(row_num, col_num, str(row[col_num]), style = xlwt.easyxf('pattern: pattern solid, fore_colour white; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
            else:
                ws.write(row_num, col_num, row[col_num], style = xlwt.easyxf('pattern: pattern solid, fore_colour white; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
        for col_num in range(6,len(row)):
            if isinstance(row[col_num], datetime.date):
                if row[col_num].weekday() == 0:
                    ws.write(row_num, col_num, " ", style = xlwt.easyxf('pattern: pattern solid, fore_colour red; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
                elif row[col_num].weekday() == 1:
                    ws.write(row_num, col_num, " ", style = xlwt.easyxf('pattern: pattern solid, fore_colour blue; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
                elif row[col_num].weekday() == 2:
                    ws.write(row_num, col_num, " ", style = xlwt.easyxf('pattern: pattern solid, fore_colour green; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
                elif row[col_num].weekday() == 3:
                    ws.write(row_num, col_num, " ", style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
                elif row[col_num].weekday() == 4:
                    ws.write(row_num, col_num, " ", style = xlwt.easyxf('pattern: pattern solid, fore_colour orange; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
                elif row[col_num].weekday() == 5 or row[col_num].weekday() == 6:
                    ws.write(row_num, col_num, " ", style = xlwt.easyxf('pattern: pattern solid, fore_colour gray25; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
                elif row[col_num] == None:
                    ws.write(row_num, col_num, " ", style = xlwt.easyxf('pattern: pattern solid, fore_colour white; font: bold True; borders: left thin, right thin, top thin, bottom thin'))  

    # Day -> Color Key                      
    ws.write(0,27, 'Monday', style = xlwt.easyxf('pattern: pattern solid, fore_colour red; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
    ws.write(1,27, 'Tuesday', style = xlwt.easyxf('pattern: pattern solid, fore_colour blue; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
    ws.write(2,27, 'Wednesday', style = xlwt.easyxf('pattern: pattern solid, fore_colour green; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
    ws.write(3,27, 'Thursday', style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
    ws.write(4,27, 'Friday', style = xlwt.easyxf('pattern: pattern solid, fore_colour orange; font: bold True; borders: left thin, right thin, top thin, bottom thin'))
    ws.write(5,27, 'Weekend', style = xlwt.easyxf('pattern: pattern solid, fore_colour gray25; font: bold True; borders: left thin, right thin, top thin, bottom thin'))

    wb.save(response)
    
    return response