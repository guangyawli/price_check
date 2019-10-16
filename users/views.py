from django.shortcuts import render
# from users.models import student
# Create your views here.
# from django.contrib.auth.models import User
from django.http import HttpResponse


# def hello_world(request):
#     return HttpResponse("Hello World!")
#
#
# def add_user(request):
#     username = request.GET.get('username')
#     cuser = student.objects.create(cname=username)
#     cuser.save()
#     return HttpResponse(cuser.cname)
#
#
# def del_user(request):
#     username = request.GET.get('username')
#     duser = student.objects.get(cname=username)
#     duser.delete()
#     return HttpResponse(duser.cname)
#
#
# def modify_user(request):
#     username = request.GET.get('username')
#     muser = student.objects.get(cname=username)
#     muser.cname = 'test'
#     muser.save()
#     return HttpResponse(muser.cname)
#
#
# def check_cookie(request):
#     if 'test_counter' not in request.COOKIES:
#         tmpcounter = 1
#         msg = 'create counter'
#     else:
#         tmpcounter = int(request.COOKIES['test_counter'])
#         tmpcounter = tmpcounter + 1
#         msg = 'counter = ' + str(tmpcounter)
#
#     res = HttpResponse(msg)
#     res.set_cookie('test_counter', tmpcounter)
#     return res
#
#
# def del_cookie(request):
#     if 'test_counter' in request.COOKIES:
#         msg = 'del counter, value = ' + str(request.COOKIES['test_counter'])
#         res = HttpResponse(msg)
#         res.delete_cookie('test_counter')
#         return res
#     else:
#         return HttpResponse('No cookie')
#
#
# def check_session(request):
#     if 'stmp_counter' not in request.session:
#         tmpcounter = 1
#         msg = 'create counter'
#     else:
#         tmpcounter = int(request.session['stmp_counter'])
#         tmpcounter = tmpcounter + 1
#         msg = 'counter = ' + str(tmpcounter)
#
#     res = HttpResponse(msg)
#     request.session['stmp_counter'] = tmpcounter
#     request.session.set_expiry(3600)
#     return res
#
#
# def del_session(request):
#     if 'stmp_counter' in request.session:
#         msg = 'del counter, value = ' + str(request.session['stmp_counter'])
#         res = HttpResponse(msg)
#         del request.session['stmp_counter']
#         return res
#     else:
#         return HttpResponse('No session')