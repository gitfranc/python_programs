##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: urls.py
# @Date: 2021-12-28 14:04:32
# @Last Modified by: franc
# @Last Modified time: 2021-12-28 19:39:48
# @Project: learning_notes
# @Use: define the url model of learning notes

from django.urls import path

from . import views

app_name = "learning_notes_apps"
urlpatterns = [
    # Homepage
    path('', views.index, name="index"),

    # Display all of topics
    path('topics/', views.topics, name='topics'),

    # The page for special topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # The used to add the new topic of page
    path('new_topic/', views.new_topic, name='new_topic'),

    # The page for special topic of new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),

    # The page for special entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),

]
