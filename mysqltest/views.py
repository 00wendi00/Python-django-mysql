from django.shortcuts import render, redirect

from mysqltest.models import UserInfo


# Create your views here.

def index(request):
    uInfo = UserInfo.objects.all()
    return render(request, 'index.html', {'userInfo': uInfo})


def adduser(request):
    uInfo = UserInfo()
    uInfo.user = 'wade'
    uInfo.pwd = '000'
    uInfo.save()
    return redirect('/index/')


def deluser(request, uid):
    u = UserInfo.objects.get(id=int(uid))
    u.delete()
    return redirect('/index/')


def edituser(request, uid):
    if request.method == 'POST':
        userid = request.POST.get('uid', None)
        user = request.POST.get('user', None)
        password = request.POST.get('pwd', None)
        uInfo = UserInfo.objects.get(id=int(userid))
        uInfo.user = user
        uInfo.pwd = password
        uInfo.save()
        return redirect('/index/')
    elif request.method == 'GET':
        uInfo = UserInfo.objects.get(id=int(uid))
        return render(request, 'edituser.html', {'userInfo': uInfo})

    return render('无此用户')
