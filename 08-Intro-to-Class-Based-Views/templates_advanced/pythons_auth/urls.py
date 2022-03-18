from django.urls import path

from pythons_auth import views

urlpatterns = (
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.PythonsLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
)
