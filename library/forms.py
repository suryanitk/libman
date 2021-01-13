from django import forms


class AddBookForm(forms.Form):
	title = forms.CharField(
			label = 'title',
		)
	author = forms.CharField(
			label = 'author',
		)
	summary = forms.CharField(
			label = 'summary',
		)
	isbn = forms.CharField(
			label = 'isbn',
		)
	genre = forms.CharField(
			label = 'genre',
		)
	language = forms.CharField(
			label = 'language',
		)
	totalcopies = forms.IntegerField(
			label = 'total copies',
		)
	availablecopies = forms.IntegerField(
			label = 'available copies',
		)

class LoginForm(forms.Form):
	username = forms.CharField(
			label = 'username',
		)

	password = forms.CharField(
			label = 'password',
		)

class RegisterForm(forms.Form):
	firstname = forms.CharField(
			label = 'firstname',
		)
	lastname = forms.CharField(
			label = 'lastname',
		)
	username = forms.CharField(
			label = 'username',
		)
	password = forms.CharField(
			label = 'password',
		)
	email = forms.CharField(
			label = 'email',
		)
	branch = forms.CharField(
			label = 'branch',
		)
	role = forms.CharField(
			label = 'role',
		)