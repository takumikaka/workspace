from django.shortcuts import render
from django.http import HttpResponse
from .models import Bugcontext

# Create your views here.

def index(request):
    bug_list = Bugcontext.objects.all().order_by('-created_time')
    return render(request, 'jira/index.html', context={'bug_list':bug_list})
    '''
    return render(request, "jira/index.html", context={
                        'title': 'JIRA',
                        'welcome': 'This is Jira.'
})
    '''
