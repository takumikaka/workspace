from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Bugcontext(models.Model):

    bug_title = models.CharField(max_length=100)
    bug_level = models.CharField(max_length=4)
    bug_author = models.ForeignKey(User,
    on_delete=models.CASCADE)
    #on_delete=models.PROTECT)
    bug_body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.bug_title
