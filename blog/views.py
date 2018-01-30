#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect ,request
from captcha import *
from .forms import *
from .models import *
# Create your views here.
#首先显示
def index(request):
    data=[]
    try:
        if request.session['username']:
            seesion=request.session['username']
            print seesion
            if seesion:
                data.append(seesion)
                print "login success!"
    except Exception , e:
        print (e)
        data.append('no login')
    title="seck"
    print request.COOKIES
    # return HttpResponse("<img id='verifycode' src='/captcha/' alt='CheckCode'/>")
    return render(request,'blog/index.html',{'title':title,'data':data},)
#验证码调用

def captcha(request):
    Cap = Captcha(request)
    Code =Cap.display()
    return Code

#注册
def register(request):
    if request.method == 'POST':
        userform =UserRegisterForm(request.POST)
        cap = request.POST.get('cap')
        ca = Captcha(request)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            if ca.check(cap):
                print "The code true"
            else:
                print "The code error!"
                return HttpResponse("验证码不正确,请刷新后重新输入！")
            if User.objects.filter(username=username):
                print "The user exits"
                return HttpResponse("用户名重复！")
            else:
                User.objects.create(username=username, password=password, email=email).save()
                return HttpResponse('register success!')
    else:
        userform = UserRegisterForm()
    return render(request,'blog/register.html',{'userform':userform,})

def login(request):

    if request.method == "POST":
        userform = UserLoginForm(request.POST)
        print userform.errors.get('username')
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user= User.objects.filter(username__exact=username,password__exact=password)
            if user:
                #Step1:生成随机字符串(seesionID)
                #Step2：通过cookie发送给客户端
                #Step3：服务端保存 session
                print "seck"
                # print user.values()[0][username]
                request.session['username']=username
                print request.session
                # return render(request,'blog/index.html',{'userform':userform})
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('用户名或者密码错误！')
    else:
        print "stsrat"
        userform=UserLoginForm()

    return render(request,'blog/login.html',{'userform':userform})
def sign_out(request):
    del request.session['username']
    return HttpResponseRedirect('/')