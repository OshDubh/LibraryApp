from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
 path('', view_all_books, name='all_books'), # homepage
 path('books/', view_all_books, name='all_books'), # homepage with url
 path('books/<int:bookid>/', view_single_book, name='single_book'), # one book
 path('books/year/<int:year>/', view_books_by_year, name='book_by_year'), # all books by year
 path('books/category/<str:cat>/', view_books_by_category, name='book_by_category'), # all books by category
 path('books/category/<str:cat>/year/<int:year>/', view_books_by_year_and_category, name='book_by_year_and_category'), # books by both
 path('books/by_category', view_all_categories, name = "all_categories"), # books filtered into category sections
 path('books', view_search_results, name = "search_results"), # for displaying search results
 path('customers/', view_all_customers, name='all_customers'), # # all customers
 path('customers/<int:customer_id>/', view_single_customer, name="single_customer"), # one customer
 path('books/add/', submit_book, name='submit_book'), # for submitting a new book to the library
 path('books/edit/<int:bookid>/', edit_book, name='edit_book'), # for edditing the details of an existing book
 path('add', api_add, name = 'api_add'), # for using an api to add numbers
 path('subtract', api_subtract, name = 'api_subtract'), # for using an api to subtract numbers
 path('divide', api_divide, name = 'api_divide'), # for using an api to divide numbers
 path('multiply', api_multiply, name = 'api_multiply'), # for using an api to multiply numbers
 path('exponential', api_exponential, name = 'api_exponential'), # for using an api to get the exponent of two numbers
]