from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
import xlrd
from .models import Tcourse, Emails, MailServer
from django.http import HttpResponse
from users.forms import UploadExcelForm
# Email
from django.core.mail import EmailMultiAlternatives, get_connection


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


def send_mails(request):
    if request.user.is_staff is False:
        return HttpResponse(' No permission ! ')
    else:
        tmp_users = User.objects.all()
        target_mails = []
        for tmp_user in tmp_users:
            target_mails.append(tmp_user.email)

        # print(target_mails)
        test_from = Emails.objects.get(e_status='default').e_from
        test_title = Emails.objects.get(e_status='default').e_title
        test_content = Emails.objects.get(e_status='default').e_content

        # context = {'dashboard_url': 'https://www.openedu.tw/dashboard4t/index', 'insight_url': 'https://insights.openedu.tw/courses/'}
        # email_template_name = 'mail_temp.html'
        # t = loader.get_template(email_template_name)
        mail_list = target_mails

        tmp_server = MailServer.objects.get(id=1)

        conn = get_connection()
        conn.username = tmp_server.m_user              # username
        conn.password = tmp_server.m_password          # password
        conn.host = tmp_server.m_server                # mail server
        conn.open()

        subject, from_email, to = test_title, test_from, mail_list
        html_content = str(test_content) #t.render(dict(context))
        msg = EmailMultiAlternatives(subject, html_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")

        conn.send_messages([msg, ])  # send_messages发送邮件
        conn.close()

        return HttpResponse('send mail ok')
