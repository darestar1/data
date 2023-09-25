"""
URL configuration for data project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('observations/', views.observation_list, name='observation_list'),
    path('observations/create/', views.observation_create, name='observation_create'),
    
    path('rocks/update/<int:rock_id>/', views.rock_update, name='rock_update'),


    
    
    path('observations/list/readonly/', views.observation_list_readonly, name='observation_list_readonly'),

    path('observations/delete/', views.delete_observation, name='delete_observation'),
    path('rocks/', views.rock_list, name='rock_list'),
    path('rocks/create/', views.rock_create, name='rock_create'),
    path('observation/update/<int:observation_id>/', views.observation_update, name='observation_update'),
    path('rocks/delete/', views.delete_rock, name='rock_delete'),
    path('rocks/update/', views.rock_list, name='rock_list'),
    path('observations/', views.observation_list, name='observation_list'),
    path('observations/update/', views.observation_update_selected, name='observation_update_selected'),
]
