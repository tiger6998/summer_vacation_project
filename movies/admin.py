from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Movies)
admin.site.register(People)
admin.site.register(UserProfile)
admin.site.register(MoviePicture)
admin.site.register(CastandCrew)