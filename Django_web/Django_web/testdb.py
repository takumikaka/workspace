# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test

# SQL operation
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>Add SQL Succesful!</p>")
