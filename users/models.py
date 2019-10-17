from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Tcourse(models.Model):
  dash_id = models.CharField(max_length=20, blank=False, unique=True, default='test0001')
  course_id = models.CharField(max_length=50, blank=False, unique=True)
  course_name = models.CharField(max_length=80, blank=True)
  tstaff = models.ManyToManyField(User, blank=False)


class Emails(models.Model):
  e_receive = models.CharField(max_length=200, blank=False, default='default')
  atitle = models.CharField(max_length=100, blank=False, default='default')
  acontent = RichTextField(blank=True, null=True)
  astatus = models.CharField(max_length=50, blank=True)

