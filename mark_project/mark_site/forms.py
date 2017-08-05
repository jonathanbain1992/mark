from django import forms
from models import *
from django.forms import ModelForm
from models import Booking

#@XXX: THIS IS FUCKED FIX TOMORROW
class BookingForm(ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data


    #def verify_age():
    #    print False
    #    return False


    #    if self.Meta.fields[4] >=18:


    #    i = 0

    #    num = ""
    #    numbers = ['0','1','2','3','4','5','6','7','8','9']
    #    paininass = str(self.__getitem__(self.Meta.fields[4]))

    #    while i < len(paininass):
    #        if paininass[i] in numbers:
    #            num+= paininass[i]
    #        i+=1

    #    return int(num) >=18



    class Meta:
        model=Booking
        fields=['booking_hours','booking_type','first_name','last_name','your_age','child_first_name','child_last_name',"childs_age",'booking_mua','booking_stylist','booking_sunbed','booking_comments']
    def clean_rowname(self):
        return self.cleaned_data['childs_age','your_age'] or None
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['childs_age'].required = False
        self.fields['your_age'].required = False



 #XXX: okay i know this method is absolutely shit and unscalable but i couldn't find a reasonable method
 # to check a person's age inside the form. I couldn't just get a value because it's a boundFieldObject or
 # whatever. So much casting was involved here. Probably remove this if anyone is using this code and doesn't need the
 # age verificaiton (or knows a better way in which case PLEASE tell me).
