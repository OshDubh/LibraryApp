from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Book, Customer, Borrow
from .forms import BookForm
from django.db.models import Q # allow results matching different types
import datetime # for filtering if the borrow is active
from django.http import JsonResponse # for the api-
from rest_framework import viewsets # import for rest api
from .serializers import * # import for rest api

# a page to display all the books in the library
def view_all_books(request):
	all_books = Book.objects.all()

	# Dynamic list of categories for the navbar categories
	categories = []

	for book in all_books:
		if book.category not in categories:
			categories.append(book.category)

	return render(request, 'all_books.html', {'books':all_books, 'categories': categories} )

def view_all_customers(request):
	all_customers = Customer.objects.all()
	all_books = Book.objects.all()

	# Dynamic list of categories for the navbar categories
	categories = []

	for book in all_books:
		if book.category not in categories:
			categories.append(book.category)

	return render(request, 'all_customers.html', {'customers': all_customers, 'books':all_books, 'categories': categories} )

# the page to view when we want to see the details on just one book
def view_single_book(request, bookid):
	single_book = get_object_or_404(Book, id=bookid)

	# get a list of people currently borrowing
	borrows = Borrow.objects.filter(book_id=single_book, due_date__gte=datetime.date.today())

	return render(request, 'single_book.html', {'book':single_book, "borrows": borrows})

# the page to view when we want to see the details on just one customer
def view_single_customer(request, customer_id):
	single_customer = get_object_or_404(Customer, id=customer_id)

	# get a list of people currently borrowing
	borrows_all = Borrow.objects.filter(customer_id=single_customer)
	borrows_current = Borrow.objects.filter(customer_id=single_customer, due_date__gte=datetime.date.today())
	borrows_past = Borrow.objects.filter(customer_id=single_customer, due_date__lt=datetime.date.today())

	return render(request, 'single_customer.html', {'customer':single_customer, "borrows_all": borrows_all, 'borrows_current': borrows_current, 'borrows_past': borrows_past})

# view a page of all the books by year, exact year does not matter
def view_books_by_year(request, year):
	books_by_year = Book.objects.filter(year__icontains=year,) # get a filtered list of the books
	all_books = Book.objects.all()

	# Dynamic list of categories for the navbar categories
	categories = []

	for book in all_books:
		if book.category not in categories:
			categories.append(book.category)

	return render(request, 'all_books.html', {'books':books_by_year, 'categories': categories})

# a page with all the views by category, search does not need to match the category exactly 
def view_books_by_category(request, cat):
	books_by_category = Book.objects.filter(category__icontains=cat,) # get a filtered list of the books
	all_books = Book.objects.all()

	# Dynamic list of categories for the navbar categories
	categories = []

	for book in all_books:
		if book.category not in categories:
			categories.append(book.category)

	return render(request, 'books_by_category.html', {'books':books_by_category, 'categories': categories, 'category': cat})

# a page with the books filtered by year and category. Does not need to match options exactly
def view_books_by_year_and_category(request, cat, year):
	books_by_year_and_category = Book.objects.filter(year__icontains = year, category__icontains = cat)
	all_books = Book.objects.all()

	# Dynamic list of categories for the navbar categories
	categories = []

	for book in all_books:
		if book.category not in categories:
			categories.append(book.category)

	return render(request, 'all_books.html', {'books':books_by_year_and_category, 'categories': categories})

# the page with all the books by category
def view_all_categories(request):
	all_books = Book.objects.all()

	# get a list of all the categories
	categories = []

	for book in all_books:
		if book.category not in categories:
			categories.append(book.category)

	return render(request, 'all_books_by_category.html', {'books':all_books, 'categories': categories})

# show matching search results for what they searched for 
def view_search_results(request):
	search = request.GET.get('search')
	all_books = Book.objects.all()

	# Dynamic list of categories for the navbar categories
	categories = []

	for book in all_books:
		if book.category not in categories:
			categories.append(book.category)

	# exit if no search
	if not search:
		return render(request,'all_books.html', {'books': all_books, 'categories': categories})

	matching_books = Book.objects.filter(Q(year__icontains = search) | Q(author__icontains = search) | Q(title__icontains = search) | Q(category__icontains = search))

	if search != "":
		return render(request, 'search_results.html', {'books':matching_books, 'categories': categories, 'search': search} )
	else:
		return render(request,'all_books.html', {'books': all_books, 'categories': categories})

# The "Add a Book" form
def submit_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save()
            return render(request, 'submit_book_success.html', {'book':book})
        else:
            return render(request, 'submit_book.html', {'form': form})
    else:
        # normal get reuqest, user wants to see the form 
        form = BookForm()
        return render(request, 'submit_book.html', {'form': form})

# edit the details of an existing book
def edit_book(request, bookid):
	book = get_object_or_404(Book, id=bookid) # load the employee object

	if request.method=="POST":
		form = BookForm(request.POST, instance=book)

		if form.is_valid():
			form.save()
			return render(request, 'edit_book_success.html', {'book':book})

		else:
			return render(request, 'submit_book.html', {'form':form})

	else:
		form = BookForm(instance=book)
		return render(request, 'submit_book.html', {'form':form})


# calculator api
# adding
def api_add(request):
	# get the numbers from the  request
	num1 = float(request.GET.get('num1', 1)) # get what num1= in the url, else default to 1
	num2 = float(request.GET.get('num2', 1)) # the url will be ../add?num1=x&num2=y

	result = num1 + num2
	response = {'result': result} # we format it as a dict so the result is a json (the standard)
	return JsonResponse(response)

def api_subtract(request):
	# get the numbers from the  request
	num1 = float(request.GET.get('num1', 1)) # get what num1= in the url, else default to 1
	num2 = float(request.GET.get('num2', 1)) # the url will be ../add?num1=x&num2=y

	result = num1 - num2
	response = {'result': result} # we format it as a dict so the result is a json (the standard)
	return JsonResponse(response)

def api_divide(request):
	# get the numbers from the  request
	num1 = float(request.GET.get('num1', 1)) # get what num1= in the url, else default to 1
	num2 = float(request.GET.get('num2', 1)) # the url will be ../add?num1=x&num2=y

	result = num1 / num2
	response = {'result': result} # we format it as a dict so the result is a json (the standard)
	return JsonResponse(response)

def api_multiply(request):
	# get the numbers from the  request
	num1 = float(request.GET.get('num1', 1)) # get what num1= in the url, else default to 1
	num2 = float(request.GET.get('num2', 1)) # the url will be ../add?num1=x&num2=y

	result = num1 * num2
	response = {'result': result} # we format it as a dict so the result is a json (the standard)
	return JsonResponse(response)

def api_exponential(request):
	# get the numbers from the  request
	num1 = float(request.GET.get('num1', 1)) # get what num1= in the url, else default to 1
	num2 = float(request.GET.get('num2', 1)) # the url will be ../add?num1=x&num2=y

	result = num1 ** num2
	response = {'result': result} # we format it as a dict so the result is a json (the standard)
	return JsonResponse(response)


# rest api stuff
class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()

class BorrowViewSet(viewsets.ModelViewSet):
	serializer_class = BorrowSerializer
	queryset = Borrow.objects.all()