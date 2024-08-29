from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('login/', views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path('register/', views.register, name="register"),
    path('detail/', views.detail, name="detail")
]