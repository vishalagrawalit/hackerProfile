from django import forms
from .models import Hacker, BasicInfo, SkillSet


class ProfileEdit(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

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
            'email',
            'password',
        ]


class BasicInfoEdit(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = [
            'best_known_as',
            'twitter',
            'facebook',
            'linkedin',
            'website',
        ]


class SkillSetEdit(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SkillSet
        fields = [
            'skill1',
            'percent1',
            'skill2',
            'percent2',
            'skill3',
            'percent3',
            'skill4',
            'percent4',
            'skill5',
            'percent5',
            'skill6',
            'percent6',
            'skill7',
            'percent7',
            'skill8',
            'percent8',
        ]


class password_tester(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hacker
        fields = [
            'password',
        ]


class profile_edit_tester(forms.ModelForm):

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
            'email',
        ]