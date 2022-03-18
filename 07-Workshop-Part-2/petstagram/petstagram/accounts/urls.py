from django.urls import path
from petstagram.accounts.views import login_view, logout_view, register_view, profile_detail_view

urlpatterns = (
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_detail_view, name='profile details'),
)
