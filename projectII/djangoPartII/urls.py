from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.help, name='helping'),
    re_path(r'^research$', views.research, name='research')
]
