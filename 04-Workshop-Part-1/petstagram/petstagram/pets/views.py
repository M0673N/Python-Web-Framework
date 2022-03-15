import os

from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import CreatePetForm
from petstagram.pets.models import Pet, Like


def pet_all(request):
    pets = Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(pet=pet, comment=form.cleaned_data['comment'])
            comment.save()
            return redirect('pet details', pet.id)
    else:
        context = {'pet': pet, 'likes': pet.like_set.count(), 'comments': pet.comment_set.all(), 'form': CommentForm()}
        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.save()
    return redirect('pet details', pet.id)


def create_pet(request):
    if request.method == 'POST':
        form = CreatePetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet list')
        return render(request, 'pet_create.html', {'form': form})
    else:
        return render(request, 'pet_create.html', {'form': CreatePetForm()})


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


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet list')
    else:
        return render(request, 'pet_delete.html', {'pet': pet})
