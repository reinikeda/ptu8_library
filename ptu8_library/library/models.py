from datetime import date
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
import uuid

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(_('name'), max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')


class Author(models.Model):
    first_name = models.CharField(_('first name'), max_length=100, db_index=True)
    last_name = models.CharField(_('last name'), max_length=100, db_index=True)
    description = HTMLField(_('description'), max_length=4000, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('author')
        verbose_name_plural = _('authors')
    
    def display_books(self):
        return ', '.join(book.title for book in self.books.all())
    display_books.short_description = _('books')


class Book(models.Model):
    title = models.CharField(_('title'), max_length=255, db_index=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='books',
        verbose_name=_('author')
    )
    summary = HTMLField(_('summary'), max_length=4000, null=True, blank=True)
    genre = models.ManyToManyField(
        Genre,
        help_text=_('select genre(s) for this book'),
        verbose_name=_('genre(s)')
    )
    cover = models.ImageField(_("cover"), upload_to='library/covers/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"
    
    class Meta:
        ordering = ['title']
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all())
    display_genre.short_description = _('genre(s)')


class BookInstance(models.Model):
    id = models.UUIDField(
        _('ID'), 
        primary_key=True, 
        default=uuid.uuid4, 
        help_text=_('Unique ID for a book copy')
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_instances',
        verbose_name=_('book'),
    )
    due_back = models.DateField(_('due back'), null=True, blank=True, db_index=True)

    LOAN_STATUS = (
        ('m', _('managed')),
        ('r', _('reserved')),
        ('t', _('taken')),
        ('a', _('available')),
        ('u', _('unavailable')),
    )

    status = models.CharField(_('status'), max_length=1, choices=LOAN_STATUS, default='a')
    reader = models.ForeignKey(
        User, 
        verbose_name=_("reader"), 
        on_delete=models.SET_NULL,
        related_name='book_instances',
        null=True, blank=True,
    )

    def __str__(self) -> str:
        return f"{self.id}: {self.book}"
    
    @property
    def is_overdue(self):
        if self.due_back:
            return self.due_back < date.today()
        return False
    
    class Meta:
        ordering = ['due_back']
        verbose_name = _('book instance')
        verbose_name_plural = _('book instances')


class BookReview(models.Model):
    book = models.ForeignKey(
        Book, 
        verbose_name=_("book"), 
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    reviewer = models.ForeignKey(
        User, 
        verbose_name=_("reviewer"), 
        on_delete=models.SET_NULL,
        related_name='book_reviews',
        null=True, blank=True,
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    content = models.TextField(_("content"), max_length=4000)

    def __str__(self) -> str:
        return f"{self.reviewer} - {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('book review')
        verbose_name_plural = _('book reviews')
