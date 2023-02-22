from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Genre(models.Model):
    name = models.CharField(_('name'), max_length=50)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    first_name = models.CharField(_('first_name'), max_length=100, db_index=True)
    last_name = models.CharField(_('last_name'), max_length=100, db_index=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['last_name', 'first_name']

class Book(models.Model):
    title = models.CharField(_('title'), max_length=255, db_index=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='books',
        verbose_name=_('author')
    )
    summary = models.TextField(_('summary'), max_length=4000, null=True, blank=True)
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 symbols <a href="https://www.isbn-international.org/content/what-isbn">ISBN codes</a>'
    )
    genre = models.ManyToManyField(
        Genre,
        help_text=_('select genre(s) for this book')
    )

    def __str__(self) -> str:
        return f'{self.author} {self.title}'

    class Meta:
        ordering = ['title']

class BookInstance(models.Model):
    id = models.UUIDField(
        _('ID'),
        primary_key=True,
        default=uuid.uuid4,
        help_text=_('Unique ID for book copy')
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_instances',
        verbose_name=_('book')
    )
    due_back = models.DurationField(_('due back'), null=True, blank=True, db_index=True)

    LOAN_STATUS = (
        ('m', _('managed')),
        ('r', _('reserved')),
        ('t', _('taken')),
        ('a', _('available')),
        ('u', _('unavailable')),
    )
    
    status = models.CharField(_('status'), max_length=1, choices=LOAN_STATUS, default='a')

    def __str__(self) -> str:
        return f'{self.id}: {self.book}'

    class Meta:
        ordering = ['due_back']