from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addemployee, name='add_employee'),
    path('view/', views.viewemployee, name='view_employee'),
    path('delete/<int:id>/', views.deleteemployee, name='delete_employee'),
]
