from django.urls import path
from .import views
urlpatterns = [
   
    path('register/',views.register, name = 'register'),
    # path('login/',views.user_login, name = 'login'),
    path('login/',views.UserLoginView.as_view(), name = 'login'),
    # path('logout/',views.user_logout, name = 'logout'),
    path('logout/',views.UserLogoutView.as_view(), name = 'logout'),
    path('profile/',views.user_profile, name = 'profile'),
    path('update_profile/',views.update_user_profile, name = 'update_profile'),
    path('password_change/',views.pass_change, name = 'pass_change'),

   
]
