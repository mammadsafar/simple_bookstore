from django.urls import path, include

from .views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    # path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
]
