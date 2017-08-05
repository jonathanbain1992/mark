# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mark_site import models

# Register your models here.
admin.site.register(models.PageBlueprint)
admin.site.register(models.ServicesBluePrint)
admin.site.register(models.PortfolioPhoto)
admin.site.register(models.Name)


class BookingAdmin(admin.ModelAdmin):
    readonly_fields=('booking_time_submission',)
admin.site.register(models.Booking,BookingAdmin)
