from django.contrib.auth.models import User
from django.db import models


class tprofile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)


class Tcourse(models.Model):
  course_id = models.CharField(max_length=50, blank=False, unique=True)
  tstaff = models.ManyToManyField(tprofile, blank=False)


class Announcements(models.Model):
  acontent = models.CharField(max_length=100, blank=False)
  aclass = models.CharField(max_length=50, blank=False)