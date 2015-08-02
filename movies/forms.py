from django import forms
from django.contrib.auth.models import User
from movies.models import *

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movies
		fields = ('name', 'release_date', 'Genre', 'runtime', 'storyline', 'picture')

class PeopleForm(forms.ModelForm):
	class Meta:
		model = People
		fields = ('name', 'career', 'intro', 'born', 'photo')		
		

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)
		
class MovieCommentsForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('comment',)