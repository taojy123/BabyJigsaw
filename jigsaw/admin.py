from django.contrib import admin

from jigsaw.models import Picture


@admin.register(Picture)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'pic')
