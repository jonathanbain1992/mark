# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class PageBlueprint(models.Model):
    page_name = models.TextField(max_length=10)
    title = models.TextField(max_length=50)
    info = models.TextField(max_length=500)
    def __unicode__(self):
        return self.page_name

class ServicesBluePrint(models.Model):
    service_name = models.TextField(max_length=30)
    service_desc = models.TextField(max_length=250)
    rate = models.FloatField()
    def __unicode__(self):
        return self.service_name

#@XXX THIS IS FUCKED FIX TOMORROW
class Booking(models.Model):
    standard = 29.99
    premium = 39.99
    bookingchoices = ((standard,"Standard"),(premium,"Premium"),(standard,"Standard [PARENTAL BOOKING]"),(premium,'Premium [PARENTAL BOOKING]'))
    booking_type=models.FloatField(choices=bookingchoices)
    booking_hours=models.FloatField()
    booking_mua = models.BooleanField(default=False, verbose_name="MUA")
    booking_stylist = models.BooleanField(default=False, verbose_name="Stylist")
    booking_sunbed = models.BooleanField(default=False, verbose_name="sunbed")
    first_name=models.CharField(max_length=30, default="firstname" )
    last_name=models.CharField(max_length=30, default="lastname")
    your_age = models.PositiveIntegerField(null=True)
    childs_age = models.PositiveIntegerField(null=True)
    booking_comments=models.TextField(max_length=100)
    fee = models.FloatField()
    child_first_name = models.CharField(max_length=80, default="note: only required when booking for a person under 18.")
    child_last_name = models.CharField(max_length=80 ,default="note: only required when booking for a person under 18.")
    booking_time_submission = models.DateTimeField(auto_now=True)




    def save(self):
        if not self.id:
            self.fee = (self.booking_hours*self.booking_type)


        super(Booking, self).save()



    def __unicode__(self):
        return self.first_name

class Name(models.Model):
    name = models.TextField(max_length=30)
    address = models.TextField(max_length=200, default="i have no home lol")
    age = models.TextField(max_length=10)
    telephone = models.TextField(max_length=10)
    def __unicode__(self):
        return self.name



class PortfolioPhoto(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField()

    def __unicode__(self):
        return self.image.name
