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
    return render(request, "create.html", context)


def update(request, id=None):
    if request.method == "POST":
        instance = get_object_or_404(Hacker, id=id)

        # CodeChef
        CC = instance.CodeChef_username
        CC = codechef(CC)
        instance.CodeChef_problem = CC[0]
        instance.CodeChef_rating = CC[1]

        # CodeForces
        CF = instance.CodeForces_username
        CF = codeforces(CF)
        instance.CodeForces_contest = CF[0]
        instance.CodeForces_rating = CF[1]

        # HackerEarth
        HE = instance.HackerEarth_username
        HE = hackerEarth(HE)
        instance.HackerEarth_problem = HE[0]
        instance.HackerEarth_rating = HE[1]

        # HackerRank
        HR = instance.HackerRank_username
        HR = hackerrank(HR)
        instance.HackerRank_problem = HR[0]
        instance.HackerRank_rating = HR[1]

        # SPOJ
        SP = instance.SPOJ_username
        SP = spoj(SP)
        instance.SPOJ_problem = SP[0]
        instance.SPOJ_rating = SP[1]

        instance.problems_solved = CC[0] + HE[0] + HR[0] + SP[0]
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
    counter = instance.profile_view
    counter += 1
    instance.profile_view = counter
    instance.save()
    
    return render(request, "profile.html", context)

def index(request):
    return render(request, "index.html", {})