from django.contrib import admin
from users.models import Tcourse, Emails, MailServer


class TcourseAdmin(admin.ModelAdmin):
    list_display = ('dash_id', 'course_id', 'course_name')


class EmailsAdmin(admin.ModelAdmin):
    list_display = ('e_from', 'e_title', 'e_content', 'e_status')


class MailServerAdmin(admin.ModelAdmin):
    list_display = ('m_server', 'm_user', 'm_password')


admin.site.register(Tcourse, TcourseAdmin)
admin.site.register(Emails, EmailsAdmin)
admin.site.register(MailServer, MailServerAdmin)

