from django.shortcuts import render
from django.http import HttpResponse

from main.models import Match


def homepage(request):
    return render(request, template_name='main/home.html', context={'matches': Match.objects.all})
