from django.db import models


# Create your models here.
class Hacker(models.Model):
    display_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=150, default="Vishal Agrawal")
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
    problems_solved = models.IntegerField(default=0, null=True, blank=True)
    ratings = models.IntegerField(default=0, null=True, blank=True)
    profile_view = models.IntegerField(default=0)

    def __str__(self):
        return str(self.display_name)
