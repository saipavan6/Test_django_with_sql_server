from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Otregister

def index(request):
    mydata = Otregister.objects.all()
    context = {
        'mymembers': mydata,
    }

    return render(request,'test.html',context)

def test():
    mydata = Otregister.objects.all()
    for i in mydata:
        print(i)

    return HttpResponse("Hello, Pavan.")
