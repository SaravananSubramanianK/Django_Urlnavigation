from django.shortcuts import render

# Create your views here.


def saran(request):
    return render(request,'one.html')

def logi(request):
    return render(request,'two.html')

def sree(request):
    return render(request,'three.html')
