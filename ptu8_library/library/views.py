from django.shortcuts import render
from . import models


def index(request):
    book_count = models.Book.objects.count()
    book_instance_count = models.BookInstance.objects.count()
    available_bi_count = models.BookInstance.objects.filter(status='a').count()
    author_count = models.Author.objects.count()
    return render(request, 'library/index.html', {
        'book_count': book_count,
        'book_instance_count': book_instance_count,
        'available_bi_count': available_bi_count,
        'author_count': author_count,
    })
