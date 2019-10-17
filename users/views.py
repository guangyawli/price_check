from django.shortcuts import render
# from users.models import student
# Create your views here.
from django.contrib.auth.models import User
import xlrd
from .models import Tcourse
from django.http import HttpResponse
from users.forms import UploadExcelForm


def ximport(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            table = wb.sheets()[0]
            row = table.nrows
            for i in range(1, row):
                col = table.row_values(i)
                if not User.objects.filter(username=col[3], email=col[4]).exists():
                    tmp_user = User.objects.create(username=col[3], email=col[4])
                if not Tcourse.objects.filter(dash_id=col[0]).exists():
                    tmp_course = Tcourse.objects.create(dash_id=col[0], course_id=col[1])
                    Tcourse.objects.get(course_id=col[1]).tstaff.add(tmp_user)

            return HttpResponse('OK')
        else:
            return HttpResponse('invalid file type')

    return render(request, "uploadfile.html", locals())