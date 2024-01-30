from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='manager-home'),
    path('manager-home', views.home, name='manager-home'),
    path('diesel-purchase', views.addDieselPurchaseRecord, name='diesel-purchase'),
    path('diesel-list', views.diesel_list, name='diesel-list'),
    path('add-worklog', views.addWorkLog, name='add-worklog'),
    path('log-list', views.log_list, name='log-list'),
    path('expenses-list', views.expense_list, name='expenses-list'),
    path('add-expense', views.addOtherExpense, name='add-expense'),
    path('movelog-list', views.Move_log_list, name='movelog-list'),
    path('add-movelog', views.add_movelog, name='add-movelog')
    
]