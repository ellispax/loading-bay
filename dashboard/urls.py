from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('show-equipment', views.equipment_view, name='show-equipment'),
    path('equipment-add', views.add_equipment, name='equipment-add'),
    path('update-equipment/<int:pk>', views.updatestatus, name='update-equipment')
]