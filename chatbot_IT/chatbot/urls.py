# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^index',views.index,name='index'),
        url(r'^submission/$',views.querySubmission,name='querySubmission'),
        url(r'^addition/$',views.queryAddition,name='queryAddition'),
        url(r'^submit_ans/$',views.sub_ans,name='sub_ans'),
        url(r'^feedback/$',views.feedback,name='feedback'),
        url(r'^save/$',views.save_changes,name='save'),]