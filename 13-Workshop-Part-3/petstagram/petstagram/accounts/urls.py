from django.urls import path
from petstagram.accounts import views

urlpatterns = (
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileDetailsView.as_view(), name='profile details'),
)
