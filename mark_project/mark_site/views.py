# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import *
from django.http import HttpResponse
from django.views import View
from models import *

# Create your views here.




class index(View):
    def get(self, request):
		msg = "index"
		context = {"msg": msg}
		return render(request, "home.html", context)
