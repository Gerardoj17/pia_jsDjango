from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('Academica/',views.Academica,name="Academica"),
    path('Ceremonial/',views.Ceremonial,name="Ceremonial"),
    path('Comercial/',views.Comercial,name="Comercial"),
    path('Publicitaria/',views.Publicitaria,name="Publicitaria"),
    path('RegistrarFeedback/', views.RegistrarFeedback, name="RegistrarFeedback")
]
