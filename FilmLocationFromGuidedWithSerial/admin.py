from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to FilmLocationFromGuidedWithSerial


class FilmLocationFromGuidedWithSerialAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


admin.site.register(models.FilmLocationFromGuidedWithSerial, FilmLocationFromGuidedWithSerialAdmin)
admin.site.register(models.Comment)
