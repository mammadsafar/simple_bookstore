from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import CostumeBookUpdate


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    form_class = CostumeBookUpdate


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    form_class = CostumeBookUpdate


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
