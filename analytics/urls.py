from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='analytics-home'),
    path('analytics-home', views.home, name='analytics-home'),
    path('diesel-graph', views.diesel_purchase_graph, name='diesel-graph'),
    path('income-graph', views.income_graph, name='income-graph'),
    # path('working-hr-charts', views.work_hours, name='working-hr-charts')
]