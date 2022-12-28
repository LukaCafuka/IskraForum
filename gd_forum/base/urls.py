from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('thread/<str:pk>/', views.thread, name="thread"),
    path('user/<str:name>/', views.user_view, name="user_view"),
    path('create-thread/', views.create_thread, name="create-thread"),
    path('delete-thread/<str:pk>/', views.delete_thread, name="delete-thread"),
    path('login/', views.login_user, name="login"),
]
