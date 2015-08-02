from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import *
from movies.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	movie_list = Movies.objects.order_by('-likes')[:5]
	people_list = People.objects.all()[:5]
	context_dict = {'movies':movie_list, 'people':people_list}
	if request.user.is_authenticated():
		try:
			user = User.objects.get(username=request.user)
			userprofile = UserProfile.objects.get(user=user)
			context_dict['userprofile'] = userprofile
		except UserProfile.DoesNotExist:
			pass
	return render(request, 'movies/index.html', context_dict)

def about(request):
	context_dict = {}
	return render(request, 'movies/about.html', context_dict)

@login_required
def add_movie(request):
	
	added = False
	
	if request.method == 'POST':
		movie_form = MovieForm(data=request.POST)
		if movie_form.is_valid():
			movie = movie_form.save(commit=False)
			
			if 'picture' in request.FILES:
				movie.picture = request.FILES['picture']
			movie.save()
			added = True
			
		else:
			print movie_form.errors
			
	else:
		movie_form = MovieForm()
	
	return render(request, 'movies/add_movie.html',{'movie_form':movie_form, 'added':added})
	
def movie(request, movie_name_slug):
	context_dict = {}
	
	try:
		movie = Movies.objects.get(slug=movie_name_slug)
		context_dict['movie_name'] = movie.name
		context_dict['movie'] = movie
	except Movies.DoesNotExist:
		print "here is the problem"
		pass
	if movie:
		try:
			moviepicture = MoviePicture.objects.filter(movie=movie)
			context_dict['moviepicture'] = moviepicture
		except MoviePicture.DoesNotExist:
			print "here is the second problem"
			pass	
		try:
			comments = Comments.objects.filter(movie=movie)
			context_dict['comments'] = comments
		except:
			pass
	return render(request, 'movies/movie.html', context_dict)
	
def register(request):
	
	registered = False
	
	if request.method == 'POST':
	
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				print request.FILES['picture']
			else:
				print "what the fu**"
			profile.save()
			
			registered = True
			
		else:
			print user_form.errors, profile_form.errors
			
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	
	return render(request, 'movies/register.html', {'user_form':user_form, 'profile_form': profile_form, 'registered':registered})
	
def user_login(request):
	if request.method == 'POST':
	
		username = request.POST.get('username')
		password = request.POST.get('password')
	
		user = authenticate(username=username, password=password)
	
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/movie')
			else:
				return HttpResponse("Your are DEAD")
		else:
			print "Invalid login details: {0}, {1}".format(username,password)
			return HttpResponse("Invalid login details supplied.")
		
	else:
		return render(request,'movies/login.html',{})
		
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/movie/')

@login_required
def add_comment(request, movie_name_slug):
	
	added = False
	
	print movie_name_slug
	

	if request.method == 'POST':
		comment_form = MovieCommentsForm(data=request.POST)
		if comment_form.is_valid():
			user = User.objects.get(username=request.user)
			try:
				movie = Movies.objects.get(slug=movie_name_slug)
			except Movies.DoesNotExist:
				print "here is the problem" + movie_name_slug
				pass
			if movie:
				comment = comment_form.save(commit=False)
				comment.user = user
				comment.movie = movie
				comment.save()
				added = True
		else:
			print comment_form.errors
	else: 
		comment_form = MovieCommentsForm()
		
	return render(request, 'movies/add_comment.html',{'comment_form':comment_form, 'added':added, 'movie_name_slug':movie_name_slug})
	