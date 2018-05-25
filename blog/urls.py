#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:seck
@time: 2018/01/03
"""
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'$',views.index,name='index'),
    url(r'^xjnuonepiecedetective/$')
]
