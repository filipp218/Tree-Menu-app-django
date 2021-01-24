from django.shortcuts import render
from django.views.generic.base import View
from yum.models import menu_item

# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request, "yum/base.html")
