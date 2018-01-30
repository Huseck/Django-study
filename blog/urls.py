#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
author:seck
time: 2018/01/28
"""
from django.conf.urls import include, url
from views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_week_6.views.home', name='home'),
    url(r'^captcha/$',captcha),
    url(r'^login/$',login),
    url(r'^register/$',register),
    url(r'^sign_out/$',sign_out),
    url(r'', index,name='index'),
]