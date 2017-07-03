#XXX: Don't make any more views here, this is the default root for the application.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class default(View):
    def get(self, request):

        msg = "go away"

        context = {"msg": msg}
        # <view logic>
        return render(request, "base.html", context)
