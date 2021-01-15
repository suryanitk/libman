from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm, AddBookForm
from .models import Users, Book, UserBook
import datetime

def index(request):
	return render(request,'index.html')

def profile(request):
	username = request.session.get('username')
	user = Users.objects.get(username = username)
	return render(request, 'profile.html', {'user':user})

def dashboard(request):
	username = request.session.get('username')
	user = Users.objects.get(username=username)
	return render(request, 'dashboard.html', {'user':user})

def addbook(request):
	if request.method == 'POST':
		form = AddBookForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data.get('title')
			author = form.cleaned_data.get('author')
			summary = form.cleaned_data.get('summary')
			isbn = form.cleaned_data.get('isbn')
			genre = form.cleaned_data.get('genre')
			language = form.cleaned_data.get('language')
			totalcopies = form.cleaned_data.get('totalcopies')
			availablecopies = form.cleaned_data.get('availablecopies')
			if availablecopies>totalcopies:
				availablecopies=totalcopies

			#create new object of model and save the details
			book, created = Book.objects.get_or_create(isbn = isbn)
			if created == True:
				book.title=title
				book.author=author
				book.summary=summary
				book.isbn=isbn
				book.genre=genre
				book.language=language
				book.totalcopies=totalcopies
				book.availablecopies=availablecopies
				book.save()

			return render(request, 'addbooksuccess.html', {'book':book})

		else:
			return HttpResponse("Invalid form")
	
	else:
		form = AddBookForm()

	return render(request, 'addbook.html', {'form':form})

def viewbook(request):
	username = request.session.get('username')
	book = Book.objects.all()
	user = Users.objects.get(username=username)

	return render(request, 'viewbook.html', {'book':book, 'user':user})

def viewstudent(request):
	username = request.session.get('username')
	book = Book.objects.all()
	user = Users.objects.get(username=username)
	
	students = Users.objects.filter(role='Student')

	return render(request, 'viewstudent.html', {'book':book, 'user':user, 'students':students})

def viewfaculty(request):
	username = request.session.get('username')
	book = Book.objects.all()
	user = Users.objects.get(username=username)

	faculty = Users.objects.filter(role='Faculty')

	return render(request, 'viewfaculty.html', {'book':book, 'user':user, 'faculty':faculty})

def issuebook(request):
	username = request.session.get('username')
	book = Book.objects.all()
	user = Users.objects.get(username=username)

	if request.method == 'POST':
		isbn = request.POST.get('issue')
		b = Book.objects.get(isbn=isbn)

		
		userbook, created = UserBook.objects.get_or_create(
			username = username,
			isbn = isbn)

		if created == True and b.availablecopies>0:
	
			userbook.username = username
			userbook.isbn = isbn
			userbook.issueddate = datetime.datetime.now()
			userbook.save()
			b.availablecopies=b.availablecopies-1
			b.save()

			return render(request, 'issuesuccess.html', {'book':b})

	return render(request, 'issuebook.html', {'book':book, 'user':user})

def issuedbook(request):
	username = request.session.get('username')
	user = Users.objects.get(username=username)
	ub = UserBook.objects.all()
	if not ub:
		return render(request, 'issuedbook.html', {'user':user, 'ub':False})
	
	ub = UserBook.objects.filter(username=username)
	if not ub:
		return render(request, 'issuedbook.html', {'user':user, 'ub':False})
	
	isbnList = []
	for i in ub:
		isbnList.append((i.isbn))
	book = Book.objects.filter(isbn__in = isbnList)

	return render(request, 'issuedbook.html', {'book':book, 'user':user, 'ub':ub})

def returnbook(request):
	username = request.session.get('username')
	user = Users.objects.get(username=username)

	#If no books issued
	ub = UserBook.objects.all()
	if not ub:
		return render(request, 'returnbook.html', {'user':user, 'ub':False})
	
	ub = UserBook.objects.filter(username=username)
	if not ub:
		return render(request, 'returnbook.html', {'user':user, 'ub':False})

	isbnList = []
	for i in ub:
		isbnList.append((i.isbn))
	book = Book.objects.filter(isbn__in = isbnList)

	if request.method == 'POST':
		isbn = request.POST.get('return')
		b = Book.objects.get(isbn=isbn)
		UserBook.objects.get(username = username, isbn = isbn).delete()
		b.availablecopies=b.availablecopies+1
		b.save()

		return render(request, 'returnsuccess.html', {'book':b})

	return render(request, 'returnbook.html', {'book':book, 'user':user, 'ub':ub})

def deletebook(request):
	username = request.session.get('username')
	book = Book.objects.all()
	user = Users.objects.get(username=username)

	if request.method == 'POST':
		isbn = request.POST.get('delete')
		Book.objects.get(isbn = isbn).delete()

		#removing all the books issued with the above isbn
		UserBook.objects.filter(isbn = isbn).delete()


	return render(request, 'deletebook.html', {'book':book, 'user':user})

def login(request):

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			
			request.session['username'] = username

			try:
				user = Users.objects.get(username = username)
			except:
				user = None

			if not user:
				isValid = False
				return render(request, 'loginfailure.html', {'isValid':isValid})

			if user.password == password:
				isValid = True
				return render(request, 'login_success.html', {'user':user, 'isValid':isValid})
			else:
				isValid = False
				return render(request, 'loginfailure.html', {'isValid':isValid})

		else:
			return HttpResponse("Invalid form")

	else:
		form = LoginForm()

	return render(request, 'login.html', {'form':form})

def addstudent(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			firstname = form.cleaned_data.get('firstname')
			lastname = form.cleaned_data.get('lastname')
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			branch = form.cleaned_data.get('branch')
			role = form.cleaned_data.get('role')

			#create new object of model and save the details
			user, created = Users.objects.get_or_create(username = username)
			if created == True:
				user.firstname=firstname
				user.lastname=lastname
				user.username=username
				user.password=password
				user.email=email
				user.branch=branch
				user.role=role
				user.save()

			return render(request, 'registersuccess.html', {'user':user})

		else:
			return HttpResponse("Invalid form")
		
	else:
		form = RegisterForm()

	return render(request, 'addstudent.html', {'form':form})