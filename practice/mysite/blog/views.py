from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticles

# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})

def blog_context(request, context_id):
    context = BlogArticles.objects.get(id=context_id)
    pub = context.publish
    return render(request, "blog/content.html", {"context": context, "publish": pub})
