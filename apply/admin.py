from django.contrib import admin
from .models import Apply

# Register your models here.
class Lay_apply(admin.ModelAdmin):
    list_display = ('name', 'grade', 'major')
admin.site.register(Apply)