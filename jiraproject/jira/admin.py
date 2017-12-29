from django.contrib import admin
from jira.models import Category, Buglevel

# Register your models here.
admin.site.register(Category)
admin.site.register(Buglevel)
