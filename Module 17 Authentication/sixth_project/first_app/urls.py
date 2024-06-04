from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',views.userlogin,name = 'login'),
    path('logout/',views.userlogout,name = 'logout'),
    path('profile/',views.profile,name = 'profile'),
    path('passchange/',views.pass_change,name = 'passchange'),
    path('passchange2/',views.pass_change2,name = 'passchange2'),
]
