from django.urls import path
from app import views

app_name='app'

urlpatterns=[
    path('sree/',views.sree,name='sree')

]