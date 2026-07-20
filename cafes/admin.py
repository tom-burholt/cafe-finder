from django.contrib import admin

# Register your models here.
from .models import Cafe
from .models import Barrio
from .models import Reviewer

admin.site.register(Cafe)
admin.site.register(Barrio)
admin.site.register(Reviewer)