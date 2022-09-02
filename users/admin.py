from django.contrib import admin
from users.models import Nxproduct
# from users.models import Tcourse, Emails, MailServer, Tprofile, EdxKey


class NxproductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'new_buy', 'license_price', 'Annual_maintain_Price','Yearly_Sub_Price', 'data_import')
    search_fields = ['product_id']
#
#
# class TcourseAdmin(admin.ModelAdmin):
#     list_display = ('dash_id', 'course_id', 'course_name', 'start_date', 'end_date')
#
#
# class EmailsAdmin(admin.ModelAdmin):
#     list_display = ('e_from', 'e_title', 'e_content', 'e_status')
#
#
# class MailServerAdmin(admin.ModelAdmin):
#     list_display = ('m_server', 'm_user', 'm_password')
#
#
# class TprofileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'cancel_flag', 'cancel_reason')
#
#
# class EdxKeyAdmin(admin.ModelAdmin):
#     list_display = ('auth_code',)
#
#


admin.site.register(Nxproduct, NxproductAdmin)
# admin.site.register(Emails, EmailsAdmin)
# admin.site.register(MailServer, MailServerAdmin)
# admin.site.register(Tprofile, TprofileAdmin)
# admin.site.register(EdxKey, EdxKeyAdmin)

