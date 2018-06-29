#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : url.py.py
# @Author: Wade Cheung
# @Date  : 2018/6/29
# @Desc  :

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^adduser/$', views.adduser),
    url(r'^deluser(.+)/$', views.deluser),
    url(r'^edituser(.+)/$', views.edituser),
]
