from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to helycenter


class helycenterAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


admin.site.register(models.HelpCenter, helycenterAdmin)
admin.site.register(models.Comment)
