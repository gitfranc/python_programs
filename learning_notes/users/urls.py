##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: urls.py
# @Date: 2021-12-28 19:47:52
# @Last Modified by: franc
# @Last Modified time: 2021-12-28 21:34:04
# @Project: learning_notes
# @Use: The urls for the users

from django.urls import path, include

from . import views


app_name = "users"
urlpatterns = [
    # defalut auth url
    path('', include("django.contrib.auth.urls")),

    # register page url
    path('register/', views.register, name='register')
]
