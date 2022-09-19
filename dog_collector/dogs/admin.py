from django.contrib import admin
from .models import Collar, Dog, Trainer

# Register your models here.

admin.site.register(Dog)
admin.site.register(Trainer)
admin.site.register(Collar)