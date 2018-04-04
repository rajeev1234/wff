from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


# class RatingInline(admin.TabularInline):
#     model = models.ActorRating

# attaching commment stack to post


# class ActorAdmin(admin.ModelAdmin):
#         inlines = [RatingInline]

# calling in admin panel


admin.site.register(models.Actors)