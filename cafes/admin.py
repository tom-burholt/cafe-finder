from django.contrib import admin

from .models import Barrio, Cafe, Dish, Review, Reviewer, Tag

admin.site.register(Cafe)
admin.site.register(Barrio)
admin.site.register(Reviewer)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Dish)
