from django.contrib import admin

from world.models import WorldBorder

admin.site.register(WorldBorder, admin.ModelAdmin)
