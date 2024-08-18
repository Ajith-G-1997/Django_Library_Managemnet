from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import (
    BookListView, BookDetailView, BookCreateView, 
    BookUpdateView, BookDeleteView, LoanListView, 
    LoanDetailView, LoanCreateView, LoanUpdateView, 
    LoanDeleteView,IndexView,RegisterView, LoginView, LogoutView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    
    path('loans/', LoanListView.as_view(), name='loan_list'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan_detail'),
    path('loan/new/', LoanCreateView.as_view(), name='loan_create'),
    path('loan/<int:pk>/edit/', LoanUpdateView.as_view(), name='loan_edit'),
    path('loan/<int:pk>/delete/', LoanDeleteView.as_view(), name='loan_delete'),
]
