from app2.views import *
from django.urls import path
app_name='someting'
urlpatterns=[
    path("ram/",ram,name="ram"),
    path("jyothi/",jyothi,name="jyothi"),

]