from django.contrib import admin
from users.models import Tcourse, Announcements

# Register your models here.
admin.site.register(Tcourse)
admin.site.register(Announcements)