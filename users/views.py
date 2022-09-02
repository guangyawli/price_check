#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
import xlrd
from .models import Nxproduct
# from .models import Tcourse, Emails, MailServer, Tprofile, EdxKey
# from django.http import HttpResponse, HttpResponseRedirect
from users.forms import UploadExcelForm
from django.db.models import Q
# Email
# from django.core.mail import EmailMultiAlternatives, get_connection
# from django.template import loader
# from proj1.settings import STATIC_ROOT, BASE_DIR
from datetime import date,datetime

import logging

#import json
import requests


def search(request):
    discount = 100;
    if request.method == 'POST':
        tmp_ids = str(request.POST['my_target_id']).lower().split(',')
        discount = request.POST['my_target_discount']
        q1 = Q()
        q1.connector = 'OR'  # 连接方式
        for x in tmp_ids:
            q1.children.append(('product_id', x))

        data = Nxproduct.objects.filter(q1)
        if not data.exists():
            err_msg = '查無資訊'
    else:
        data = []

    return render(request, "search_list.html", locals())


def check_id(request, nxid):
    if Nxproduct.objects.filter(product_id=nxid).exists():
        tmp = Nxproduct.objects.get(product_id=nxid)
        data = {
            "Product ID": tmp.product_id,
            "License定價(單價)":tmp.license_price,
            "年度維護定價(單價)":tmp.Annual_maintain_Price
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    else:
        data = {
            "status": "產品不存在"
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def ximport(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            table = wb.sheets()[0]
            row = table.nrows
            for i in range(1, row):
                col = table.row_values(i)
                # print(col)
                if col[22]=="":
                    col[22] = 0
                if col[25]=="":
                    col[25]=0
                if col[28] == "":
                    col[28] = 0
                if not Nxproduct.objects.filter(product_id=col[5]).exists():
                    if col[5] != "":
                        obj, created = Nxproduct.objects.update_or_create(product_id=str(col[5]).lower(), product_name=col[6],
                                    license_price=float(col[22]), Yearly_Sub_Price=float(col[25])*12, Annual_maintain_Price=float(col[28]),
                                    new_buy=float(col[22])+float(col[28]))
                else:
                    tmp_product = Nxproduct.objects.get(product_id=col[5])
                    if col[25] == "":
                         tmp_product.Yearly_Sub_Price = 0
                    else:
                        if tmp_product.license_price != float(col[22]) or tmp_product.Annual_maintain_Price != float(col[28]) \
                                or tmp_product.Yearly_Sub_Price != float(col[25])*12 or \
                                tmp_product.new_buy !=float(col[22])+float(col[28]):

                            tmp_product.product_id=str(col[5]).lower()
                            tmp_product.product_name=col[6]
                            tmp_product.license_price=float(col[22])
                            tmp_product.Yearly_Sub_Price = float(col[25])*12
                            tmp_product.Annual_maintain_Price= float(col[28])
                            tmp_product.new_buy=float(col[22])+float(col[28])
                            tmp_product.save()

            err_msg = 'import data ok'
            return render(request, "ihome.html", locals())
        else:
            err_msg = 'invalid file type'
            return render(request, "ihome.html", locals())

    return render(request, "uploadfile.html", locals())


# def oimport(request):
#     if request.user.is_staff is False:
#         err_msg = 'No permission !'
#         return render(request, "ihome.html", locals())
#     else:
#         if request.method == 'POST':
#             form = UploadExcelForm(request.POST, request.FILES)
#             if form.is_valid():
#                 wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
#                 table = wb.sheets()[0]
#                 row = table.nrows
#                 for i in range(1, row):
#                     col = table.row_values(i)
#                     print(col)
#
#                     # if not User.objects.filter(username=col[3]).exists():
#                     #     tmp_user = User.objects.create(username=col[3], email=col[4])
#                     # else:
#                     #     tmp_user = User.objects.get(username=col[3])
#                     # if not Tcourse.objects.filter(dash_id=col[0]).exists():
#                     #     date1 = datetime.datetime.strptime(col[5], '%Y-%m-%d')
#                     #     date2 = datetime.datetime.strptime(col[6], '%Y-%m-%d')
#                     #     tmp_course = Tcourse.objects.create(dash_id=col[0], course_id=col[1], course_name=col[2],
#                     #                                         start_date=date1, end_date=date2)
#                     # else:
#                     #     tmp_course = Tcourse.objects.get(dash_id=col[0], course_id=col[1])
#                     #
#                     # if tmp_user not in Tcourse.objects.get(course_id=col[1]).tstaff.all():
#                     #     Tcourse.objects.get(course_id=col[1]).tstaff.add(tmp_user)
#
#                 err_msg = 'import data ok'
#                 return render(request, "ihome.html", locals())
#             else:
#                 err_msg = 'invalid file type'
#                 return render(request, "ihome.html", locals())
#
#         return render(request, "uploadfile.html", locals())


# def send_mails(request):
#     if request.user.is_staff is False:
#         err_msg = 'No permission !'
#         return render(request, "ihome.html", locals())
#     else:
#         Schedule.objects.create(
#             func='users.views.send_mails_ii',
#             name='send_mail_once',
#             repeats=1,
#             next_run=datetime.datetime.now()
#         )
#         err_msg = 'send mail ok'
#         return render(request, "ihome.html", locals())
#

def home(request):
    return render(request, "ihome.html", locals())


def cancel_inform(request):
    return HttpResponse('此功能停用，請洽管理員')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
