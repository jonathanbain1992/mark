# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import *
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import FormView
from models import *
from forms import *
from jonathan_exceptions import *

# Create your views here.




class index(View):
    def get(self, request):

        data = PageBlueprint.objects.get(page_name="homepage")

        context = {"data":data}
        return render(request, "home.html", context)


class services(View):
    def get(self, request):

        data = ServicesBluePrint.objects.filter().order_by('service_priority')

        context = {"data":data}
        return render(request, "services.html", context)


class gallery(View):
    def get(self, request):

        data = PortfolioPhoto.objects.all()
        context = {"data":data}
        return render(request, "gallery.html", context)



class book(View):

    form = BookingForm
    model = form.Meta.model
    template_name = "book.html"

    ##@XXX THIS IS ALL FUCKED> FIX IT PLS.
    def get(self,request,*args,**kwargs):
        form = self.form()
        return render(request,self.template_name,{"form":form})

    def post(self,request,*args,**kwargs):
        form = self.form(request.POST)

        if form.is_valid():
            form.clean()
            form.full_clean()
            form.save(commit=False)
            numbers = ['1','2','3','4','5','6','7','8','9','10']
            agefield = ""
            childagefield = ""
            agefieldmetadata = str(form.__getitem__(form.Meta.fields[4]))
            childagefieldmetadata = str(form.__getitem__(form.Meta.fields[7]))
            i = 0
            while i < len(agefieldmetadata):
                if agefieldmetadata[i] in numbers:
                    agefield+= agefieldmetadata[i]
                i+=1
            i=0
            while i < len(childagefieldmetadata):
                if childagefieldmetadata[i] in numbers:
                    childagefield += childagefieldmetadata[i]
                i+=1

            if len(agefield)==0:
                return HttpResponse("please enter your age")

            elif int(agefield)>=18 and len(childagefield)==0:
                form.save(commit=True)
                return HttpResponse("Booking Accepted")
            elif int(agefield)>=18:
                if (int(childagefield)>=16 and int(childagefield)<18):
                    form.save(commit=True)
                    return HttpResponse("Booking Accepted")
                else:
                    return HttpResponse("child age invalid")
            else:
                return HttpResponse("you are too young.")
        else:
            return HttpResponse("Invalid input (have you put a negative number in the age field?)")

        #    if int(agefield) <= 18 and len(childagefield) == 0:
        #        return HttpResponse("You are not old enough to book for yourself")
        #    elif int(agefield) >= 18 and (int(childagefield) <=16 or int(childagefield) >= 18):
        #        return HttpResponse("You are old enough to book for a child however the child must be between 16 and 18 inclusive.")
        #    elif int(agefield) >= 18 and len(childagefield) ==0:
        #        form.save(commit=True)
        #        return HttpResponse('adult booking accepted')
        #    elif int(agefield) >= 18 and (int(childagefield)>=16 and int(childagefield)<=18):
        #        form.save(commit=True)
        #        return HttpResponse("child booking accepted")
        #    else:
        #        print childagefield, len(childagefield)
        #        return HttpResponse('booking rejected for unknown reason')
