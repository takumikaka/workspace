from django.shortcuts import render
from django.http import HttpResponse
from .models import Bugcontext

# Create your views here.

def jira_title(request):
    jiras = Bugcontext.objects.all()
    return render(request, "jira/titles.html", {"jiras": jiras})
