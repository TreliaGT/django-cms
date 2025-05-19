from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # Pages URLs
    path('pages/', views.page_list, name='page_list'),
    # path('pages/<int:pk>/', views.page_detail, name='page_detail'),
    # path('pages/create/', views.page_create, name='page_create'),
    # path('pages/<int:pk>/edit/', views.page_edit, name='page_edit'),
    # path('pages/<int:pk>/delete/', views.page_delete, name='page_delete'),

    # Post Types URLs
    path('post-types/', views.posttype_list, name='posttype_list'),
    # path('post-types/<int:pk>/', views.posttype_detail, name='posttype_detail'),
    # path('post-types/create/', views.posttype_create, name='posttype_create'),
    # path('post-types/<int:pk>/edit/', views.posttype_edit, name='posttype_edit'),
    # path('post-types/<int:pk>/delete/', views.posttype_delete, name='posttype_delete'),

    # Media URLs
    path('media/', views.media_list, name='media_list'),
    # path('media/<int:pk>/', views.media_detail, name='media_detail'),
    # path('media/create/', views.media_create, name='media_create'),
    # path('media/<int:pk>/edit/', views.media_edit, name='media_edit'),
    # path('media/<int:pk>/delete/', views.media_delete, name='media_delete'),

    # Navigation URLs
    path('navigation/', views.navigation_list, name='navigation_list'),
    # path('navigation/<int:pk>/', views.navigation_detail, name='navigation_detail'),
    # path('navigation/create/', views.navigation_create, name='navigation_create'),
    # path('navigation/<int:pk>/edit/', views.navigation_edit, name='navigation_edit'),
    # path('navigation/<int:pk>/delete/', views.navigation_delete, name='navigation_delete'),

]