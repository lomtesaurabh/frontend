# helloworld_project/urls.py

from django.urls import path
from helloworld.views import hello_world

urlpatterns = [
    path('', hello_world),
]
