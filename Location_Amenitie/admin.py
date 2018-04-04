from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to Location_Amenitie


class Location_AmenitieAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


admin.site.register(models.Location_Amenitie, Location_AmenitieAdmin)
admin.site.register(models.Comment)
