#XXX: Don't make any more views here, this is the default root for the application.
from django.shortcuts import render
from django.http import HttpResponse


def default(request):
    return HttpResponse("go away.")