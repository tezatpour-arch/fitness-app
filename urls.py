from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # اضافه کن
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('training/beginner/', views.beginner_training, name='beginner'),
    path('training/intermediate/', views.intermediate_training, name='intermediate'),
    path('training/advanced/', views.advanced_training, name='advanced'),
    path('nutrition/beginner/', views.beginner_nutrition, name='nutrition_beginner'),
    path('nutrition/intermediate/', views.intermediate_nutrition, name='nutrition_intermediate'),
    path('nutrition/advanced/', views.advanced_nutrition, name='nutrition_advanced'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('workout/<str:level>/', views.workout_view, name='workout_level'),
    path('nutrition/<str:level>/', views.nutrition_view, name='nutrition_level'),


]
