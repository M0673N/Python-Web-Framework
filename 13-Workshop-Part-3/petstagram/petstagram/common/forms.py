from django import forms

from petstagram.common.models import Comment
from petstagram.mixins import BootstrapFormMixin


class CommentForm(forms.ModelForm, BootstrapFormMixin):
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-2'
    }))

    class Meta:
        model = Comment
        fields = ['text']
