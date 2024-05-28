from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('contact/',views.contact),
    path('practise_page/',views.practise_page),
]
