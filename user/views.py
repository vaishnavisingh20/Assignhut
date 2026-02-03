from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import datetime
# create connection from django to write manual queries
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'user/index.html')
def about(request):
    return render(request, 'user/about.html')
def contact(request):
    s=False
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('mob')
        c=request.POST.get('email')
        d=request.POST.get('msg')
        contactInfo(Name=a,Mobile=b,Email=c,Msg=d).save()
        s=True
    return render(request, 'user/contact.html', context={"msg":s})
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('passwd')
        currentuser=myregister.objects.filter(email=email,passwd=password)
        if currentuser:
            request.session['course']=str(currentuser[0].course)
            request.session['sem']=str(currentuser[0].year)
            request.session['name']=str(currentuser[0].name)
            request.session['pic']=str(currentuser[0].pic)
            request.session['user']=email
            return HttpResponse("<script>alert('Log in successful');window.location.href='/user/index/';</script>")
        else:
            return HttpResponse("<script>alert('User id and password mismatch');window.location.href='/user/index/';</script>")
    return render(request, 'user/login.html')
def signin(request):
    s = False
    if request.method == "POST":
        a = request.POST.get('rollno')
        b = request.POST.get('name')
        c = request.POST.get('mobile')
        d = request.POST.get('email')
        e = request.POST.get('password')
        f = request.POST.get('course')
        g = request.POST.get('year')
        h = request.FILES.get('pic')
        myregister(rno=a, name=b, mobile=c, email=d, passwd=e, course=f, year=g, pic=h).save()
        s = True
    mydict = {"status": s}
    return render(request, 'user/signin.html',mydict)
def gallery(request):
    x=ugallery.objects.all().order_by('-id')
    mydict={"data":x}
    return render(request, 'user/gallery.html',mydict)
def myassignment(request):
    if request.session.get('user'):
        course=request.session.get('course')
        sem=request.session.get('sem')
        assignment=assignmenttbl.objects.filter(status='True').order_by('id')
    else:
        return HttpResponse("<script>alert('Log in first');window.location.href='/user/login/';</script>")
    return render(request, 'user/myassignment.html',{'assignment':assignment})
def logout(request):
    del request.session['user']
    return render(request, 'user/index.html')
def assignmentdetails(request):
    if request.GET.get('id'):
        id = request.GET.get('id')
        user=request.session.get('user')
        if request.method=='POST':
            remark=request.POST.get('remark')
            afile=request.FILES.get('afile')
            studentanswer(sid=user, asid=id, sremark=remark, sanswer=afile, marks=0, submitdate=datetime.datetime.now()).save()
            return HttpResponse("<script>alert('Assignment Submitted Successfully');window.location.href='/user/assignmentdetails?id="+id+"';</script>")
        assignment = assignmenttbl.objects.filter(id=id).order_by('-id')
        answer = studentanswer.objects.filter(sid=user,asid=id)
        return render(request, 'user/assignmentdetails.html', {'assignment': assignment,'answer':answer})
    return render(request,'user/assignmentdetails.html')
def profile(request):
    user=request.session.get('user')
    mydict={}
    if user:
        rdata=myregister.objects.all().filter(email=user)
        mydict={'rdata':rdata}
    return render(request, 'user/profile.html',mydict)
def lectures(request):
    a = request.GET.get('msg')
    ldata=lecturevideo.objects.filter(vcategory=a)
    md={'ldata':ldata}
    return render(request,'user/lectures.html',md)
def lcategory(request):

    ldata=lecturecat.objects.all().order_by('-id')
    return render(request,'user/lcategory.html',{'ldata':ldata})
def viewlecture(request):
    return render(request,'user/viewlecture.html')
def developer(request):
    return render(request,'user/developer.html')