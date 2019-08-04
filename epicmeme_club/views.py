from django.shortcuts import render, get_object_or_404, redirect

from imagesharing.models import Image


def homepage(request):
    template = "home.html"

    imageObjList = Image.objects.all()[:5]

    return render(request, template, {"imageObjList": imageObjList})

def helppage(request):
    template = "help.html"

    return render(request, template, {})

def tospage(request):
    template = "terms-of-service.html"

    return render(request, template, {})

def privacypage(request):
    template = "privacy-policy.html"

    return render(request, template, {})

