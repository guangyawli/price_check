from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

class Tprofile(models.Model):
  cancel_flag = models.CharField(max_length=10, blank=True)
  cancel_reason = models.CharField(max_length=100, blank=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)


class Tcourse(models.Model):
  dash_id = models.CharField(max_length=20, blank=False, unique=True, default='test0001')
  course_id = models.CharField(max_length=50, blank=False, unique=True)
  course_name = models.CharField(max_length=80, blank=True)
  tstaff = models.ManyToManyField(User, blank=False)
  start_date = models.DateField(default=date.today)
  end_date = models.DateField(default=date.today)


class Emails(models.Model):
  e_from = models.CharField(max_length=50, blank=False, default='default_from')
  e_title = models.CharField(max_length=100, blank=False, default='default_title')
  e_content = RichTextField(blank=True, null=True)
  e_status = models.CharField(max_length=50, blank=True)


class MailServer(models.Model):
  m_server = models.CharField(max_length=50, blank=False, default='mail.gandi.net')
  m_user = models.CharField(max_length=50, blank=False, default='test@twshop.asia')
  m_password = models.CharField(max_length=30, blank=False, default='default_password')
