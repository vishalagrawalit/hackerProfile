from django.db import models

# Create your models here.
class Hacker(models.Model):
    display_name = models.CharField(max_length=100)
    display_picture = models.ImageField(width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    CodeChef_username = models.CharField(max_length=50, null=True, blank=True)
    CodeForces_username = models.CharField(null=True, blank=True, max_length=50)
    HackerRank_username = models.CharField(null=True, blank=True, max_length=50)
    HackerEarth_username = models.CharField(null=True, blank=True, max_length=50)
    InterviewBit_username = models.CharField(null=True, blank=True, max_length=50)
    LeetCode_username = models.CharField(null=True, blank=True, max_length=50)
    SPOJ_username = models.CharField(null=True, blank=True, max_length=50)
    GitHub_username = models.CharField(null=True, blank=True, max_length=50)
    BitBucket_username = models.CharField(null=True, blank=True, max_length=50)
    problems_solved = models.IntegerField(default=0, null=True, blank=True)
    ratings = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.display_name)
