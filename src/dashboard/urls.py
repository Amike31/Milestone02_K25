from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('MulaiTes/',views.mulaites),
    path('CaraKerja/',views.carakerja),
    path('FAQ/',views.faq),
    path('InfoRS/',views.infors),
    path('Tentang/',views.tentang),
    path('ResultSafe/',views.resultsafe,name='result-safe'),
    path('ResultInfected/',views.resultinfected,name='result-infected'),
]