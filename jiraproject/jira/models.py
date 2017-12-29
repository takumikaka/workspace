from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bugid(models.Model):

    bugid_id = models.IntegerField(default=0)

class Category(models.Model):

    category_text = models.CharField(max_length=100)

    def __str__(self):
        return self.category_text

class Buglevel(models.Model):

    buglevel_text = models.CharField(max_length=30)

    def __str__(self):
        return self.buglevel_text

class Bugcontext(models.Model):

    bug_title = models.CharField(max_length=100)

    bug_body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    bug_levels = models.ManyToManyField(Buglevel, blank=True)

    '''
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    '''
