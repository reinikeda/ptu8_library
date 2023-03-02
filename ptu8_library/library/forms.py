from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = models.BookReview
        fields = ('book', 'reviewer', 'content')
        widgets = {'book': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserBookInstanceCreateForm(forms.ModelForm):
    class Meta:
        model = models.BookInstance
        fields = ('book', 'due_back', 'status')
        widgets = {
            'due_back': DateInput(),
            'status': forms.HiddenInput(),
        }


class UserBookInstanceUpdateForm(forms.ModelForm):
    class Meta:
        model = models.BookInstance
        fields = ('book', 'due_back', 'status')
        widgets = {
            'book': forms.HiddenInput(),
            'due_back': DateInput(),
            'status': forms.HiddenInput(),
        }
