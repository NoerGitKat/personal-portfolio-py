from django.shortcuts import render
from .models import ResumeProject


def home(request):
    # 1 Grab objects from DB
    projects = ResumeProject.objects.all()

    # 2 Render objects in template
    return render(request, 'index.html', {'projects': projects})
