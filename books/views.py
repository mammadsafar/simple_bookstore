from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Book
from .forms import CostumeBookUpdate, CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()
            return redirect('book_detail', pk=pk)
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {'book': book, 'comments': comments, 'comment_form': comment_form})


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = CostumeBookUpdate
    template_name = 'books/book_create.html'


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    permission_required = 'books.us'
    model = Book
    template_name = 'books/book_update.html'
    form_class = CostumeBookUpdate

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
