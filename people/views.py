from django.shortcuts import render
from django.http import HttpResponse
from movies.models import *
from movies.forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def add_people(request):
	
	added = False
	
	if request.method == 'POST':
		people_form = PeopleForm(data=request.POST)
		if people_form.is_valid():
			people = people_form.save(commit=False)
			
			if 'photo' in request.FILES:
				people.photo = request.FILES['photo']
				print "that's it!"
			else:
				print 'there it is!'
			people.save()
			added = True
			
		else:
			print people_form.errors
			
	else:
		people_form = PeopleForm()
	
	return render(request, 'people/add_people.html',{'people_form':people_form, 'added':added})
	
	
def people(request, people_name_slug):
	context_dict = {}
	
	try:
		people = People.objects.get(slug=people_name_slug)
		context_dict['people_name'] = people.name
		context_dict['people'] = people
	except People.DoesNotExist:
		print "here is the problem"
		pass
	if people:
		try:
			peoplepicture = PeoplePicture.objects.filter(people=people)
			context_dict['peoplepicture'] = peoplepicture
		except PeoplePicture.DoesNotExist:
			print "Here is the second question"
			pass
	
	return render(request, 'people/people.html', context_dict)
	
@login_required
def add_picture(request, people_name_slug):
	
	added = False
	
	if request.method == 'POST':
		picture_form = PeoplePictureForm(data=request.POST)
		if picture_form.is_valid():
			try:
				people = People.objects.get(slug=people_name_slug)
			except People.DoesNotExist:
				print "here is the problem" + people_name_slug
				pass
			if people:
				picture = picture_form.save(commit=False)
				if 'picture' in request.FILES:
					picture.picture = request.FILES['picture']
					picture.people = people
					picture.save()
					added = True
		else:
			print picture_form.errors
	else: 
		picture_form = PeoplePictureForm()
		
	return render(request, 'people/add_picture.html',
		{'picture_form':picture_form, 'added':added, 'people_name_slug':people_name_slug})
		
def peoplelist(request):
	people_list = People.objects.all()
	paginator   = Paginator(people_list, 3)
	
	page = request.GET.get('page')
	try:
		people = paginator.page(page)
	except PageNotAnInteger:
		people = paginator.page(1)
	except EmptyPage:
		people = paginator.page(paginator.num_pages)
	
	return render(request, 'people/people_list.html', {'people':people})