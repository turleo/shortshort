from django.urls import path

from . import views

urlpatterns = [
	path('<str:id>/', views.goto, name='redirect'),
	path('api/create/', views.new_from_api),
	path('', views.index_file),
]
