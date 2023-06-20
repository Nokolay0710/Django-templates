from .views import index, list, add
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^list/$', list, name='list'),
    re_path(r'^add/$', add, name='add'),
]