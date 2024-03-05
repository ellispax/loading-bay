from django.urls import path

from . import views

urlpatterns = [
	path("", views.general_info, name="settings"),

	
	path('users', views.get_users, name='users'),
  
	path('add-user', views.add_user, name='add-user'),
	

	

]