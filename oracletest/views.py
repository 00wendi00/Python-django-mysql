from django.shortcuts import render, redirect
from oracletest.models import UserInfo


# Create your views here.

def index(request):
    uInfo = UserInfo.objects.all()
    return render(request, 'index2.html', {'userInfo': uInfo})


def adduser(request):
    uInfo = UserInfo()
    uInfo.user = 'wade'
    uInfo.pwd = '000'
    uInfo.save()
    return redirect('/oracle/index/')


def deluser(request, uid):
    u = UserInfo.objects.get(id=int(uid))
    u.delete()
    return redirect('/oracle/index/')


def edituser(request, uid):
    if request.method == 'POST':
        userid = request.POST.get('uid', None)
        user = request.POST.get('user', None)
        password = request.POST.get('pwd', None)
        uInfo = UserInfo.objects.get(id=int(userid))
        uInfo.user = user
        uInfo.pwd = password
        uInfo.save()
        return redirect('/oracle/index/')
    elif request.method == 'GET':
        uInfo = UserInfo.objects.get(id=int(uid))
        return render(request, 'edituser2.html', {'userInfo': uInfo})

    return render('无此用户')
