from django.db import models


# Create your models here.
class Hacker(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=150)
    display_picture = models.ImageField(width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    CodeChef_username = models.CharField(max_length=50, null=True, blank=True)
    CodeChef_problem = models.IntegerField(default=0)
    CodeChef_rating = models.CharField(default="NA", max_length=50)
    CodeForces_username = models.CharField(null=True, blank=True, max_length=50)
    CodeForces_contest = models.IntegerField(default=0)
    CodeForces_rating = models.CharField(default="NA", max_length=50)
    HackerRank_username = models.CharField(null=True, blank=True, max_length=50)
    HackerRank_problem = models.IntegerField(default=0)
    HackerRank_rating = models.CharField(default="NA", max_length=50)
    HackerEarth_username = models.CharField(null=True, blank=True, max_length=50)
    HackerEarth_problem = models.IntegerField(default=0)
    HackerEarth_rating = models.CharField(default="NA", max_length=50)
    SPOJ_username = models.CharField(null=True, blank=True, max_length=50)
    SPOJ_problem = models.IntegerField(default=0)
    SPOJ_rating = models.CharField(default="NA", max_length=50)
    GitHub_username = models.CharField(null=True, blank=True, max_length=50)
    GitHub_repo = models.IntegerField(default=0)
    problems_solved = models.IntegerField(default=0, null=True, blank=True)
    ratings = models.IntegerField(default=0, null=True, blank=True)
    profile_view = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.display_name)


class Repository(models.Model):
    user = models.CharField(max_length=250, default="")
    repo_name = models.CharField(max_length=250, default="")
    repo_description = models.CharField(max_length=250, default="")
    repo_link = models.URLField()

    def __str__(self):
        return str(self.repo_name)


class BasicInfo(models.Model):
    user = models.CharField(max_length=250, default="", unique=True)
    best_known_as = models.CharField(max_length=250)
    twitter = models.URLField(default="", null=True, blank=True)
    facebook = models.URLField(default="",null=True, blank=True)
    linkedin = models.URLField(default="", null=True, blank=True)
    website = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return str(self.best_known_as)


class SkillSet(models.Model):
    user = models.CharField(max_length=250, default="", unique=True)
    password = models.CharField(max_length=50, default="")
    skill1 = models.CharField(max_length=250, null=True, blank=True)
    percent1 = models.IntegerField(null=True, blank=True)
    skill2 = models.CharField(max_length=250, null=True, blank=True)
    percent2 = models.IntegerField(null=True, blank=True)
    skill3 = models.CharField(max_length=250, null=True, blank=True)
    percent3 = models.IntegerField(null=True, blank=True)
    skill4 = models.CharField(max_length=250, null=True, blank=True)
    percent4 = models.IntegerField(null=True, blank=True)
    skill5 = models.CharField(max_length=250, null=True, blank=True)
    percent5 = models.IntegerField(null=True, blank=True)
    skill6 = models.CharField(max_length=250, null=True, blank=True)
    percent6 = models.IntegerField(null=True, blank=True)
    skill7 = models.CharField(max_length=250, null=True, blank=True)
    percent7 = models.IntegerField(null=True, blank=True)
    skill8 = models.CharField(max_length=250, null=True, blank=True)
    percent8 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)