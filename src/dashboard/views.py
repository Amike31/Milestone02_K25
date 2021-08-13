from django.shortcuts import redirect, render
import pickle

# Create your views here.

def index(request):
    return render(request,'index.html')
    
def mulaites(request):
    questions=[
        {'labels':'Saat ini saya sedang batuk/pilek','nameform':'cough'},
        {'labels':'Saat ini saya sedang demam','nameform':'fever'},
        {'labels':'Saat ini saya sedang merasakan sakit tenggorokan','nameform':'sore_throat'},
        {'labels':'Saat ini saya sedang kesulitan bernapas','nameform':'shortness_of_breath'},
        {'labels':'Saat ini saya sedang merasakan sakit kepala','nameform':'head_ache'},
        {'labels':'Saya berjenis kelamin laki-laki','nameform':'gender'},
        {'labels':'Saya berumur lebih dari 60 tahun','nameform':'age_60_and_above'},
        {'labels':'Saya pernah kontak dengan orang yang terinfeksi covid','nameform':'test_indication'},
        ]
    context={
        'questions':questions
    }

    if request.method=='POST':
        if request.POST.get('cough') is not None and request.POST.get('fever') is not None and request.POST.get('sore_throat') is not None and request.POST.get('shortness_of_breath') is not None and request.POST.get('head_ache') is not None and request.POST.get('age_60_and_above') is not None and request.POST.get('gender') is not None and request.POST.get('test_indication') is not None:
            model = pickle.load(open('ml_model.sav', 'rb'))
            pred=model.predict([[int(request.POST.get('cough')),int(request.POST.get('fever')),int(request.POST.get('sore_throat')),int(request.POST.get('shortness_of_breath')),int(request.POST.get('head_ache')),int(request.POST.get('age_60_and_above')),int(request.POST.get('gender')),int(request.POST.get('test_indication'))]])
            if pred[0]==1:
                return redirect('result-infected')
            else:
                return redirect('result-safe')
    return render(request,'MulaiTes.html',context)

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