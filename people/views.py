from django.shortcuts import render
from django.http import HttpResponse
from movies.models import People, Movies
from movies.forms import MovieForm, PeopleForm
from django.contrib.auth.decorators import login_required

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
			peoplepicture = PeoplePiture.objects.filter(people=people)
			context_dict['peoplepicture'] = peoplepicture
		except PeoplePiture.DoesNotExist:
			print "Here is the second question"
			pass
	
	return render(request, 'people/people.html', context_dict)