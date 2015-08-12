from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
	name = models.CharField(max_length=400)
	release_date = models.DateField()
	Genre = models.CharField(max_length=100)
	runtime = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	Genre = models.CharField(max_length=100)
	storyline = models.TextField()
	picture = models.ImageField(upload_to='media', blank=True)
	slug = models.SlugField(unique=True)
	def save(self, *args, **kwargs): 
		self.slug = slugify(self.name)
		super(Movies, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.name
		
class People(models.Model):
	name = models.CharField(max_length=150)
	careers = (
        (u'A',u"Actor"),
		(u'S',u"Actress"),
        (u'W',u"Writer"),
		(u'L',u"Director"),
    )
	career = models.CharField(max_length=1, choices=careers)
	intro = models.TextField()
	born = models.DateField()
	photo = models.ImageField(upload_to='media', blank=True)
	slug = models.SlugField(unique=True)
	def save(self, *args, **kwargs): 
		self.slug = slugify(self.name)
		super(People, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name
	
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='user', blank=True)
	
	def __unicode__(self):
		return self.user.username
		
class MoviePicture(models.Model):
	movie = models.ForeignKey(Movies)
	picture = models.ImageField(upload_to='media', blank=True)
	
	def __unicode__(self):
		return self.movie.name
		
class PeoplePicture(models.Model):
	people = models.ForeignKey(People)
	picture = models.ImageField(upload_to='media', blank=True)
	
	def __unicode__(self):
		return self.movie.name
		
class Comments(models.Model):
	user = models.ForeignKey(User)
	movie = models.ForeignKey(Movies)
	comment = models.TextField()
	date = models.DateField(default="2015-7-20")
	likes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.movie.name
		
class CastandCrew(models.Model):
	movie = models.ForeignKey(Movies)
	celebs = models.ForeignKey(People)
	positions = (
        (u'D',u"Director"),
		(u'C',u"Cast"),
        (u'W',u"Writer"),
    )
	position = models.CharField(max_length=1, choices=positions)
	
	def __unicode__(self):
		return self.movie.name + self.celebs.name

