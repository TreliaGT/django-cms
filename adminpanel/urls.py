from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/add/', views.add_user, name='add_user'),
    path('sources', views.source_list, name='source_list'),
    path('sourcesadd/', views.source_add, name='source_add'),
    path('sources/delete/<int:pk>/', views.source_delete, name='source_delete'),
]
