from django import forms
from .models import Hacker


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Hacker
        fields = [
            'display_name',
            'full_name',
            'display_picture',
            'CodeChef_username',
            'CodeForces_username',
            'HackerRank_username',
            'HackerEarth_username',
            'SPOJ_username',
            'GitHub_username',
        ]
