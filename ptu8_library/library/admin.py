from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    # readonly_fields = ('id', )
    can_delete = False
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'display_genre')
    list_display_links = ('title', )
    list_filter = ('genre', )
    inlines = (BookInstanceInline, )


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'is_overdue', 'due_back', 'reader')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (_('General'), {'fields': ('id', 'book')}),
        (_('Availability'), {'fields': (('status', 'due_back', 'reader'), )}),
    )
    search_fields = ('book__title', 'book__author__last_name', 'id', 'reader__last_name')
    list_editable = ('due_back', 'status')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'display_books')
    list_display_links = ('first_name', 'last_name')


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'book', 'reviewer', 'content')
    list_display_links = ('created_at', )
    search_fields = ('reviewer__last_name', 'book__title', 'book__author__last_name')


admin.site.register(models.Genre)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookInstance, BookInstanceAdmin)
admin.site.register(models.BookReview, BookReviewAdmin)
