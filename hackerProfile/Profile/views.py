from django.shortcuts import render, get_object_or_404
from .models import Hacker
from .forms import ProfileEdit
from .script import *


def hackerform(request):
    form = ProfileEdit(request.POST or None, request.FILES or None)

    if form.is_valid():
        CC = form.cleaned_data['CodeChef_username']
        HE = form.cleaned_data['HackerEarth_username']
        CC = codechef(CC)
        HE = hackerEarth(HE)
        instance = form.save(commit=False)
        instance.problems_solved = CC[0]
        instance.ratings = CC[1] + HE[0]
        instance.save()

        return render(request, "index.html", {})
    context = {
        "form": form,
    }
    return render(request, "index.html", context)


def update(request, id=None):
    if request.method == "POST":
        instance = get_object_or_404(Hacker, id=id)
        CC = instance.CodeChef_username
        CC = codechef(CC)
        HE = instance.HackerEarth_username
        HE = hackerEarth(HE)
        instance.problems_solved = CC[0]
        instance.ratings = HE[0] + CC[1]
        instance.save()

        instance = get_object_or_404(Hacker, id=id)
        context = {
            "instance": instance,
        }

        return render(request, "profile.html", context)
    instance = get_object_or_404(Hacker, id=id)
    context = {
        "instance": instance,
    }
    return render(request, "profile.html", context)