from django.contrib import admin
from . import models

# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ["heading","image","id"]

admin.site.register(models.Posts,AdminModel)