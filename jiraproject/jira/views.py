from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Bugcontext

# Create your views here.

def jira_title(request):
    jiras = Bugcontext.objects.all()
    return render(request, "jira/titles.html", {"jiras": jiras})

def jira_context(request, context_id):
    #context = Bugcontext.objects.get(id = context_id)
    context = get_object_or_404(Bugcontext, id=context_id)
    pub = context.publish
    return render(request, "jira/content.html", {"context": context, "publish": pub})
