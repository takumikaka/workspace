from django.shortcuts import render
from django.http import HttpResponse
from .models import Bugcontext

# Create your views here.

def bug_title(request):
    bug_titles = Bugcontext.objects.all()
    return render(request, "jira/titles.html", {"bug_titles": bug_titles})
