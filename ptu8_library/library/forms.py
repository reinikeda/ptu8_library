from django import forms
from . import models


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = models.BookReview
        fields = ('book', 'reviewer', 'content')
        widgets = {'book': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}
