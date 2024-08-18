from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Member, Loan
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'library/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'library/login.html'

class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('login')




class IndexView(TemplateView):
    template_name = 'library/index.html'

# List all books
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

# View details of a specific book
class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

# Create a new book entry
class BookCreateView(CreateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'isbn', 'publisher', 'publication_date']
    success_url = reverse_lazy('book_list')

# Update an existing book
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'isbn', 'publisher', 'publication_date']
    success_url = reverse_lazy('book_list')

# Delete a book entry
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

# List all loans
class LoanListView(ListView):
    model = Loan
    template_name = 'library/loan_list.html'
    context_object_name = 'loans'

# View details of a specific loan
class LoanDetailView(DetailView):
    model = Loan
    template_name = 'library/loan_detail.html'
    context_object_name = 'loan'

# Create a new loan entry
class LoanCreateView(CreateView):
    model = Loan
    template_name = 'library/loan_form.html'
    fields = ['book', 'member', 'loan_date', 'return_date']
    success_url = reverse_lazy('loan_list')

# Update an existing loan
class LoanUpdateView(UpdateView):
    model = Loan
    template_name = 'library/loan_form.html'
    fields = ['book', 'member', 'loan_date', 'return_date']
    success_url = reverse_lazy('loan_list')

# Delete a loan entry
class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'library/loan_confirm_delete.html'
    success_url = reverse_lazy('loan_list')
