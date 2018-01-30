#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
author:seck
time: 2018/01/28
"""
from django import forms
from .views import *
class UserRegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        error_messages={'required':'用户名不能为空'},
        label='用户名',max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Username','class':'username11'}))
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')
    # captcha1=captcha()
class UserLoginForm(forms.Form):
    username = forms.CharField(required=True,
        error_messages={'required':'用户名不能为空'},label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())