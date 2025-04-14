from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("invest_track",views.get_investment_tracking),
]