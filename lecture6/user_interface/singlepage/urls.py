from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('singlepage2/',views.singlepage2,name='singlepage2'),
    path('sections/<int:num>',views.section,name='section')
]