from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def he(request):
    return HttpResponse("Hello guys..welcome to django workshop")
def sam(request):
    return HttpResponse("<h2 style=color:blue;background-color:pink;font-size:45px;font-style:italic><center>Hello world!</center></h2>")


def dynamic(request,a,b):
    return HttpResponse("<h2 style=background-color:pink><center>My roll number is:{}and My name is :{}</h2></center>".format(a,b))


def temp(request):
    return render(request,'temp.html',{})

def table(request):
    return render(request,'table.html',{})

def data(request,id,name):
    return render(request,'details.html',{'i':id,'n':name})


#css
def inline(request):
    return render(request,'inline.html',{})
def internal(request):
    return render(request,'internal.html',{})
def external(request):
    if request.method=="POST":
        nm=request.POST['uname']
        mb=request.POST['mbl']
        em=request.POST['email']
        ps=request.POST['psw']
        cps=request.POST['cpsw']
        # print(nm,mb,em,ps,cps)
        return render(request,'data.html',{'n':nm,'m':mb,'e':em,'p':ps,'c':cps})
    return render(request,'external.html',{})
def bootstrap(request):
    return render(request,'bootstrap.html')
def offline(request):
    return render(request,'offline.html')
def register(request):
    return render(request,'register.html')
