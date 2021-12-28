##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caifeiliu
# @Email: caifei521@163.com
# @File: forms.py
# @Date: 2021-12-28 17:03:42
# @Last Modified by: franc
# @Last Modified time: 2021-12-28 19:21:17
# @Project: learning_notes
# @Use: the user topic of forms

from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """ The user topic of forms """

    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ''}

class EntryForm(forms.ModelForm):
    ''' The special of topic form '''
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ''}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}

