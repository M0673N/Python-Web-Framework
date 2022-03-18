from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import EditPetForm, CreatePetForm
from petstagram.pets.models import Pet, Like


class ListPetsView(ListView):
    template_name = 'pet_list.html'
    context_object_name = 'pets'
    model = Pet


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']

        is_owner = pet.user == self.request.user

        is_liked_by_user = pet.like_set.filter(user_id=self.request.user.id).exists()
        context['form'] = CommentForm()
        context['comments'] = pet.comment_set.all()
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user
        context['likes'] = pet.like_set.count()

        return context


class CommentPetView(LoginRequiredMixin, View):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pet = Pet.objects.get(pk=self.kwargs['pk'])
            comment = Comment(
                text=form.cleaned_data['text'],
                pet=pet,
                user=self.request.user,
            )
            comment.save()

            return redirect('pet details', pet.id)


class LikePetView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = pet.like_set.filter(user_id=self.request.user.id).first()
        if like_object_by_user:
            like_object_by_user.delete()
        else:
            like = Like(
                pet=pet,
                user=self.request.user,
            )
            like.save()
        return redirect('pet details', pet.id)


class CreatePetView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = CreatePetForm
    success_url = reverse_lazy('pet list')
    template_name = 'pet_create.html'

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


class EditPetView(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = 'pet_edit.html'
    form_class = EditPetForm
    success_url = reverse_lazy('pet list')


class DeletePetView(LoginRequiredMixin, DeleteView):
    template_name = 'pet_delete.html'
    model = Pet
    success_url = reverse_lazy('pet list')

    def post(self, request, *args, **kwargs):
        Pet.objects.get(pk=self.kwargs['pk']).image_url.delete()
        return super().post(request, *args, **kwargs)
