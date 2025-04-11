from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("invest_track",views.get_investment_tracking)
]