from django.shortcuts import render, get_object_or_404, redirect

from .models import Image
from .forms import ImageModelForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def upload_image(request):
    template = "imagesharing/upload.html"

    form = ImageModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save()
        form = ImageModelForm()

    return render(request, template, {"form": form})


def list_images(request):
    template = "imagesharing/list.html"

    imageObjList = Image.objects.all()

    return render(request, template, {"imageObjList": imageObjList})


def detail_image(request, slug):
    template = "imagesharing/detail.html"

    imageObj = get_object_or_404(Image, slug = slug)

    return render(request, template, {"imageObj": imageObj})


@staff_member_required
def delete_image(request, slug):
    template = "imagesharing/delete.html"

    imageObj = get_object_or_404(Image, slug = slug)

    if request.method == "POST":
        imageObj.delete()
        return redirect('/imagelist/')

    return render(request, template, {"imageObj": imageObj})
