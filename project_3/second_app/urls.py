from django.urls import path
from .import views
urlpatterns = [
    path('home3/',views.home),
    path('practise/',views.practise),

   
]