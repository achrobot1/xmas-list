from django import forms
from .models import Gift, UserProfile

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['description', 'gift_link']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


