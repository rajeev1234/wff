from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to amenity_addresses


class Amenity_AddressesAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


admin.site.register(models.Amenity_Adresses,Amenity_AddressesAdmin)
admin.site.register(models.Comment)
