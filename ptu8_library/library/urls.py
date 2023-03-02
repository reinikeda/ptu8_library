from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>', views.author, name='author'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book'),
    path('my/books/', views.UserBookInstnceListView.as_view(), name='user_bookinstances'),
    path('my/book/new/', views.UserBookInstanceCreateView.as_view(), name='user_bookinstance_create'),
    path('my/book/<uuid:pk>/update/', views.UserBookInstanceUpdateView.as_view(), name='user_bookinstance_update'),
    path('my/book/<uuid:pk>/delete/', views.UserBookInstanceDeleteView.as_view(), name='user_bookinstance_delete'),
]
