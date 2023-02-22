from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'display_genre')
    list_display_links = ('title', )


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (_('General'), {'fields': ('id', 'book')}),
        (_('Availability'), {'fields': (('status', 'due_back'),)}),
    )


admin.site.register(models.Genre)
admin.site.register(models.Author)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookInstance, BookInstanceAdmin)
