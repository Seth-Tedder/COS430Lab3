# -*- coding: utf-8 -*-
"""urls.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tOHax8LXKV2WENI0x9itjC01jmoqbGOX
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]