from django.urls import path
from .views import *

urlpatterns = [
    # path('login', login, name="login" ),
    path('register',register, name="register"),
    # path('register-company', create_company_user, name='create-company-user' )
]