from os import name
from django.urls import path
from . import views
app_name = 'funnels'

urlpatterns=[
    path('',views.starterforfunnel,name='starterforfunnel'),
    path('createfun/',views.createfunnel,name='createfunnel'),
    path('createseq/',views.createsequence,name='createsequence'),
    path('scheduleseq/',views.schedulesequences,name='schedulesequences'),
    path('activate/',views.startfunnel,name='startfunnel'),
    path('completed/',views.viewcompleted,name='viewcompleted'),
    path('ongoing/',views.viewongoing,name='viewongoing'),
    path('customtem/',views.customtemplate,name='customtemplate')
]