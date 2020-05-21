from django.shortcuts import render, redirect

# Create your views here.


def homepg(request) :
    return render(request,'cricapp/crichome.html')

def log(request) :
    return render(request,'cricapp/user.html')

def about(request) :
    return render(request,'cricapp/about.html')

def tuto(request) :
    return render(request,'cricapp/tutorials.html')

def auh(request) :
    un = int(request.GET["user"])
    pw = int(request.GET["pass"])
    if un==133 and pw==12345 :
        ky = 'logged in successfully'
        return render(request, 'cricapp/userlogin.html', {'status' : ky})
    else :
        ky='incorrect userid and password'
        return render(request, 'cricapp/user.html', {'status' : ky})

def cal(request) :
    mph = float(request.GET["dy"])
    kmph = mph*1.60934
    return render(request, 'cricapp/usercal.html', {'status' : kmph})