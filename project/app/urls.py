from django.urls import path
from .views import signup_view, login_view, logout_view,home,base

urlpatterns = [
    path('', base, name='base'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
]
