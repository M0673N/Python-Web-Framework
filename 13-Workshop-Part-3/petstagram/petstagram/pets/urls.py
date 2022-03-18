from django.urls import path

from petstagram.pets import views

urlpatterns = [
    path('', views.ListPetsView.as_view(), name='pet list'),
    path('details/<int:pk>', views.PetDetailsView.as_view(), name='pet details'),
    path('like/<int:pk>', views.LikePetView.as_view(), name='like pet'),
    path('create/', views.CreatePetView.as_view(), name='create pet'),
    path('edit/<int:pk>', views.EditPetView.as_view(), name='edit pet'),
    path('delete/<int:pk>', views.DeletePetView.as_view(), name='delete pet'),
    path('comment/<int:pk>', views.CommentPetView.as_view(), name='comment pet'),
]
