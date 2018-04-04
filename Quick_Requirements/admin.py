from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to Quick_Requirements


class Quick_RequirementsAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


admin.site.register(models.Quick_Requirements, Quick_RequirementsAdmin)
admin.site.register(models.Comment)
