from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView, ListView

from market.models import Book
from market.forms import BookForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        
        #if self.request.user.is_authenticated():
        books = Book.objects.order_by('-created_on')[:15]
        ctx['books'] = books
        return ctx


class NewBookView(CreateView):
    form_class = BookForm
    template_name = 'create_or_edit_book.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NewBookView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        book_obj = form.save(commit=False)
        book_obj.user = self.request.user

        book_obj.save()
        return HttpResponseRedirect(reverse('home'))


class EditBookView(UpdateView):
    form_class = BookForm
    template_name = 'create_or_edit_book.html'
    success_url = '/'
    model = Book

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EditBookView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(EditBookView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class BookDetailsView(DetailView):
    model = Book
    template_name = 'book_details.html'


class MyBooksListView(ListView):
    model = Book
    template_name = 'book_list.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MyBooksListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MyBooksListView, self).get_context_data(**kwargs)
        context['has_books'] = Book.objects.filter(user=self.request.user).exists()
        context['books'] = Book.objects.filter(user=self.request.user)
        return context
