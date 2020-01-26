from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
	path('vk/', views.vk_bot, name='redirect'),
]