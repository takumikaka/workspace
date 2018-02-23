from django.contrib import admin
from jira.models import Bugcontext

# Register your models here.
class JiraBugAdmin(admin.ModelAdmin):
    list_display = ("bug_title", "bug_author", "bug_body", "publish")
    list_filter = ("publish", "bug_author")
    search_fields = ("bug_title", "bug_body")
    #raw_id_fields = ("bug_author",)
    date_hierarchy = "publish"
    ordering = ["publish", "bug_author"]

admin.site.register(Bugcontext, JiraBugAdmin)
