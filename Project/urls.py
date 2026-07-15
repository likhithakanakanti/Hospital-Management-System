"""
URL configuration for hospital_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from hospital_app import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patients/', views.patients, name='patients'),
    path('add_patient/', views.add_patient),
    path('edit_patient/<int:id>/', views.edit_patient),
    path('delete_patient/<int:id>/', views.delete_patient),
    path('add_doctor/', views.add_doctor,name='add_doctor'),
    path('edit_doctor/<int:id>/', views.edit_doctor),
    path('doctors/',views.doctors,name='doctors'),
    path('delete_doctor/<int:id>/', views.delete_doctor),
    path('toggle_doctor/<int:id>/', views.toggle_doctor),
    path('appointment/', views.appointment),
    path('history/', views.history,name='history'),
    path('logout/', views.logout_view),
]
