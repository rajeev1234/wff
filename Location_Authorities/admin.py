from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to Location_Authoritie


class Location_AuthoritieAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


admin.site.register(models.LocationAuthority, Location_AuthoritieAdmin)
admin.site.register(models.Comment)
