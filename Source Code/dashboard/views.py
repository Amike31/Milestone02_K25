from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
    
def mulaites(request):
    return render(request,'MulaiTes.html')

def carakerja(request):
    return render(request,'CaraKerja.html')

def faq(request):
    return render(request,'FAQ.html')

def infors(request):
    return render(request,'InfoRS.html')

def tentang(request):
    return render(request,'tentang.html')

def resultsafe(request):
    return render(request,'ResultSafe.html')

def resultinfected(request):
    return render(request,'ResultInfected.html')