# -*- coding: utf-8 -*-
"""urls.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tOHax8LXKV2WENI0x9itjC01jmoqbGOX
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("usmapp/", include("usmapp.urls")),
    path('admin/', admin.site.urls),
]