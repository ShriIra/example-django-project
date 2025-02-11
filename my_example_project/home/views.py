from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime

# def home(request):
#     # return HttpResponse("Hello world!")
#     return render(request, "home/welcome.html", {'today': datetime.today()})

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {'today': datetime.today()}

# @login_required(login_url="/admin")
# def authorized(request):
#     return render(request, "home/authorized.html", {})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"
