from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Hacker, Repository, BasicInfo, SkillSet
from .forms import ProfileEdit, BasicInfoEdit, SkillSetEdit, password_tester, profile_edit_tester
from .script import *


def index(request):
    return render(request, "index.html", {})


def hackerform(request):
    form = ProfileEdit(request.POST or None, request.FILES or None)
    form1 = BasicInfoEdit(request.POST or None)

    if form.is_valid() and form1.is_valid():
        CC_user = form.cleaned_data['CodeChef_username']
        CF_user = form.cleaned_data['CodeForces_username']
        HR_user = form.cleaned_data['HackerRank_username']
        HE_user = form.cleaned_data['HackerEarth_username']
        SP_user = form.cleaned_data['SPOJ_username']
        GH_user = form.cleaned_data['GitHub_username']

        if CC_user:
            CC = codechef(CC_user)
        if CF_user:
            CF = codeforces(CF_user)
        if HR_user:
            HR = hackerrank(HR_user)
        if HE_user:
            HE = hackerEarth(HE_user)
        if SP_user:
            SP = spoj(SP_user)
        if GH_user:
            GH = github(GH_user)

        instance = form.save(commit=False)
        instance1 = form1.save(commit=False)

        if CC_user:
            instance.CodeChef_problem = CC[0]
            instance.CodeChef_rating = CC[1]
            instance.problems_solved += CC[0]
        if CF_user:
            instance.CodeForces_contest = CF[0]
            instance.CodeForces_rating = CF[1]
        if HE_user:
            instance.HackerEarth_problem = HE[0]
            instance.HackerEarth_rating = HE[1]
            instance.problems_solved += HE[0]
        if HR_user:
            instance.HackerRank_problem = HR[0]
            instance.HackerRank_rating = HR[1]
            instance.problems_solved += HR[0]
        if SP_user:
            instance.SPOJ_problem = SP[0]
            instance.SPOJ_rating = SP[1]
            instance.problems_solved += SP[0]
        if GH_user:
            instance.GitHub_repo = GH[0]

        instance.save()

        for i in range(1, len(GH)):
            if Repository.objects.filter(repo_link=GH[i][2]):
                continue
            else:
                p = Repository(user=form.cleaned_data['display_name'],
                               repo_name=GH[i][0],
                               repo_description=GH[i][1],
                               repo_link=GH[i][2])
                p.save()

        instance1.user = form.cleaned_data["display_name"]
        instance1.save()

        return HttpResponseRedirect('http://127.0.0.1:8000/create/' +
                                    str(instance.id) + "/" +
                                    instance.display_name
                                    )

    context = {
        "form": form,
        "form1": form1,
    }

    return render(request, "create.html", context)


def skillform(request, id=None, user=None):
    form = SkillSetEdit(request.POST or None)
    form2 = password_tester(request.POST or None)
    password_check = Hacker.objects.get(display_name=user)

    if form.is_valid() and form2.is_valid():
        if form2.cleaned_data['password'] == password_check['password']:
            instance = form.save(commit=False)
            instance.user = user
            instance.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/profile/' + str(id))
        else:
            context = {
                "form": form,
                "Error": "Please fill the right credentials."
            }
            return render(request, "skills.html", context)

    if len(Hacker.objects.filter(display_name__iexact=user)) == 1 and len(SkillSet.objects.filter(user__iexact=user)) == 0:
        context = {
            "form": form,
            "form2": form2,
        }
        return render(request, "skills.html", context)
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/error/')


def update(request, id=None):
    if request.method == "POST":
        instance = get_object_or_404(Hacker, id=id)

        # CodeChef
        CC = instance.CodeChef_username
        if CC:
            CC = codechef(CC)
            instance.CodeChef_problem = CC[0]
            instance.CodeChef_rating = CC[1]
            instance.problems_solved += CC[0]

        # CodeForces
        CF = instance.CodeForces_username
        if CF:
            CF = codeforces(CF)
            instance.CodeForces_contest = CF[0]
            instance.CodeForces_rating = CF[1]

        # HackerEarth
        HE = instance.HackerEarth_username
        if HE:
            HE = hackerEarth(HE)
            instance.HackerEarth_problem = HE[0]
            instance.HackerEarth_rating = HE[1]
            instance.problems_solved += HE[0]

        # HackerRank
        HR = instance.HackerRank_username
        if HR:
            HR = hackerrank(HR)
            instance.HackerRank_problem = HR[0]
            instance.HackerRank_rating = HR[1]
            instance.problems_solved += HR[0]

        # SPOJ
        SP = instance.SPOJ_username
        if SP:
            SP = spoj(SP)
            instance.SPOJ_problem = SP[0]
            instance.SPOJ_rating = SP[1]
            instance.problems_solved += SP[0]

        # Github
        GH = instance.GitHub_username
        if GH:
            GH = github(GH)
            instance.GitHub_repo = GH[0]

            for i in range(1, len(GH)):
                if Repository.objects.filter(repo_link=GH[i][2]):
                    continue
                else:
                    p = Repository(user=instance.display_name, repo_name=GH[i][0], repo_description=GH[i][1],
                                   repo_link=GH[i][2])
                    p.save()

        instance.save()

        instance = get_object_or_404(Hacker, id=id)
        if instance.GitHub_repo == 1:
            repo = Repository.objects.get(user=instance.display_name)
        else:
            repo = Repository.objects.filter(user=instance.display_name)
        basic_info = BasicInfo.objects.get(user=instance.display_name)

        context = {
            "instance": instance,
            "repo_list": repo,
            "basic_info": basic_info,
        }

        return render(request, "profile.html", context)

    instance = get_object_or_404(Hacker, id=id)
    if instance.GitHub_repo == 1:
        repo = Repository.objects.get(user=instance.display_name)
    else:
        repo = Repository.objects.filter(user=instance.display_name)
    basic_info = BasicInfo.objects.get(user=instance.display_name)
    skill_level = SkillSet.objects.get(user=instance.display_name)

    context = {
        "instance": instance,
        "repo_list": repo,
        "basic_info": basic_info,
        "skill_level": skill_level,
    }

    counter = instance.profile_view
    counter += 1
    instance.profile_view = counter
    instance.save()

    return render(request, "profile.html", context)


def editbasicInfo(request, id=None, user=None):
    instance = get_object_or_404(Hacker, id=id)
    instance1 = get_object_or_404(BasicInfo, user=user)
    form = profile_edit_tester(request.POST or None, request.FILES or None, instance=instance)
    form1 = BasicInfoEdit(request.POST or None, instance=instance1)
    form2 = password_tester(request.POST or None)

    if form.is_valid() and form1.is_valid() and form2.is_valid() and form2.cleaned_data[
        "password"] == instance.password:
        print(form2.cleaned_data["password"])
        print(instance.password)
        CC_user = form.cleaned_data['CodeChef_username']
        CF_user = form.cleaned_data['CodeForces_username']
        HR_user = form.cleaned_data['HackerRank_username']
        HE_user = form.cleaned_data['HackerEarth_username']
        SP_user = form.cleaned_data['SPOJ_username']
        GH_user = form.cleaned_data['GitHub_username']

        if CC_user:
            CC = codechef(CC_user)
        if CF_user:
            CF = codeforces(CF_user)
        if HR_user:
            HR = hackerrank(HR_user)
        if HE_user:
            HE = hackerEarth(HE_user)
        if SP_user:
            SP = spoj(SP_user)
        if GH_user:
            GH = github(GH_user)

        instance = form.save(commit=False)

        if CC_user:
            instance.CodeChef_problem = CC[0]
            instance.CodeChef_rating = CC[1]
            instance.problems_solved += CC[0]
        if CF_user:
            instance.CodeForces_contest = CF[0]
            instance.CodeForces_rating = CF[1]
        if HE_user:
            instance.HackerEarth_problem = HE[0]
            instance.HackerEarth_rating = HE[1]
            instance.problems_solved += HE[0]
        if HR_user:
            instance.HackerRank_problem = HR[0]
            instance.HackerRank_rating = HR[1]
            instance.problems_solved += HR[0]
        if SP_user:
            instance.SPOJ_problem = SP[0]
            instance.SPOJ_rating = SP[1]
            instance.problems_solved += SP[0]
        if GH_user:
            instance.GitHub_repo = GH[0]

        instance.save()

        GH = instance.GitHub_username
        if GH:
            GH = github(GH)
            instance.GitHub_repo = GH[0]

            for i in range(1, len(GH)):
                if Repository.objects.filter(repo_link=GH[i][2]):
                    continue
                else:
                    p = Repository(user=instance.display_name, repo_name=GH[i][0], repo_description=GH[i][1],
                                   repo_link=GH[i][2])
                    p.save()

        instance1 = form1.save(commit=False)
        instance.save()
        instance1.save()

        return HttpResponseRedirect('http://127.0.0.1:8000/profile/' + str(id))

    context = {
        "form": form,
        "form1": form1,
        "form2": form2,
    }
    return render(request, "edit.html", context)


def editskills(request, id=None, user=None):
    instance = get_object_or_404(SkillSet, user=user)
    instance1 = get_object_or_404(Hacker, display_name=user)
    form = SkillSetEdit(request.POST or None, instance=instance)
    form2 = password_tester(request.POST or None)

    if form.is_valid() and form2.is_valid() and form2.cleaned_data["password"] == instance1.password:
        instance = form.save(commit=False)
        instance.save()

        return HttpResponseRedirect('http://127.0.0.1:8000/profile/' + str(id))

    context = {
        "form": form,
        "form2": form2,
    }
    return render(request, "editskills.html", context)


def errorpage(request):
    return render(request, "error.html", {})