from django import forms
from .models import Person, Video, StandInformation, CustomUser

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name', 'gender', 'age', 'profession']

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class StandInformationForm(forms.ModelForm):
    class Meta:
        model = StandInformation
        fields= ["lat", "lon", "accuracy", "entwicklungsstufe", "mischungsgrad", "bemerkungen", "age"]
        widgets = {
            'bemerkungen': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            "accuracy": "Genauigkeit[m]",
            "age": "Alter in Jahren",
            "lon": "Längengrad [°]",
            "lat": "Breitengrad [°]"
        }


class CustomUserCreationForm(UserCreationForm):

    is_collector = forms.BooleanField(initial=True, required=False)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'is_collector')


class CustomUserChangeForm(UserChangeForm):

    is_collector = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_collector')