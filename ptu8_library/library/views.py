from django.shortcuts import render, get_object_or_404
from django.views import generic
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


def authors(request):
    authors = models.Author.objects.all()
    return render(request, 'library/authors.html', {
        'authors': authors,
    })

def author(request, author_id):
    author = get_object_or_404(models.Author, id=author_id)
    return render(request, 'library/author.html', {
        'author': author,
    })


class BookListView(generic.ListView):
    model = models.Book
    paginate_by = 4
    template_name = 'library/book_list.html'


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'library/book_detail.html'
