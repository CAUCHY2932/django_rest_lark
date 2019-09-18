# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/18 12:06
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
