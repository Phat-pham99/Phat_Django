from django.urls import path
from .views import signup, login_view,home,landing_page,page_401
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('signup', signup, name='signup'),
    path("", landing_page, name="landing_page"),
    path('login', login_view, name='login'),
    path('home', home, name='home'),
    path('401', page_401, name='unauthorized')
]