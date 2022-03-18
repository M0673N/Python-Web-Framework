import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from petstagram.accounts.models import UserProfile

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import CreatePetForm
from petstagram.pets.models import Pet, Like


def pet_all(request):
    pets = Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    is_owner = pet.user == request.user
    is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()
    context = {'pet': pet, 'likes': pet.like_set.count(), 'comments': pet.comment_set.all(), 'form': CommentForm,
               'is_owner': is_owner, 'is_liked': is_liked_by_user}
    return render(request, 'pet_detail.html', context)


@login_required
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    already_liked = pet.like_set.filter(user_id=request.user.id).exists()
    if already_liked:
        pet.like_set.filter(user_id=request.user.id).delete()
    else:
        like = Like(pet=pet, user=request.user)
        like.save()
    return redirect('pet details', pet.id)


@login_required
def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = UserProfile.objects.get(id=request.user.id)
        comment.pet = Pet.objects.get(pk=pk)
        comment.save()
    return redirect('pet details', pk)


@login_required(login_url=reverse_lazy('login'))
def create_pet(request):
    if request.method == 'POST':
        form = CreatePetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            form.save()
            return redirect('pet list')
        return render(request, 'pet_create.html', {'form': form})
    else:
        return render(request, 'pet_create.html', {'form': CreatePetForm})


@login_required
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        previous_image = pet.image_url
        form = CreatePetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            os.remove(previous_image.path)
            form.save()
            return redirect('pet details', pet.id)
        return render(request, 'pet_edit.html', {'form': form})
    else:
        return render(request, 'pet_edit.html', {'form': CreatePetForm(initial=pet.__dict__, instance=pet)})


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet list')
    else:
        return render(request, 'pet_delete.html', {'pet': pet})
