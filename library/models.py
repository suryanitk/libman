from django.db import models

class Book(models.Model):

	genre_choices = [
		('Fiction', 'Fiction'),
		('Magazine', 'Magazine'),
		('Novel', 'Novel'),
		('Study', 'Study'),
		('Sports', 'Sports'),
		('Biography', 'Biography'),
		('Others', 'Others')
	]

	language_choices = [
		('English', 'English'),
		('Hindi', 'Hindi'),
		('German', 'German'),
		('French', 'French'),
		('Japanese', 'Japanese'),
		('Others', 'Others')
	]

	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	summary = models.TextField(max_length=1000)
	isbn = models.CharField(max_length=13, primary_key = True, null=False)
	genre = models.CharField(choices=genre_choices, max_length=20)
	language = models.CharField(choices=language_choices, max_length=20)
	totalcopies = models.IntegerField(null=True)
	availablecopies = models.IntegerField(null=True)

	def __str__(self):
		return self.isbn

class Users(models.Model):

	role_choices = [
		('Staff', 'Staff'),
		('Faculty', 'Faculty'),
		('Student', 'Student')
	]

	branch_choices = [
		('CSE', 'CSE'),
		('ME', 'ME'),
		('EC', 'EC'),
		('CE', 'CE'),
		('EE', 'EE'),
		('NA', 'NA')
	]

	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	username = models.CharField(max_length=20, primary_key = True, null=False)
	password = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	branch = models.CharField(choices=branch_choices, max_length=30)
	role = models.CharField(choices=role_choices, max_length=10)

	def __str__(self):
		return self.username

class UserBook(models.Model):
	username = models.CharField(max_length=20)
	isbn = models.CharField(max_length=20)
	issueddate = models.DateField(null=True)

	def __str__(self):
		return self.username + '-' + self.isbn

	