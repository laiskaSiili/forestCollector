from django.forms import ModelForm, Textarea
from .models import Person, Video, StandInformation, CustomUser

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class PersonForm(ModelForm):
    class Meta:
        model=Person
        fields=['name', 'gender', 'age', 'profession']

class VideoForm(ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class StandInformationForm(ModelForm):
    class Meta:
        model = StandInformation
        fields= ["lat", "lon", "accuracy", "entwicklungsstufe", "mischungsgrad", "bemerkungen", "age"]
        widgets = {
            'bemerkungen': Textarea(attrs={'rows': 3}),
        }
        labels = {
            "accuracy": "Genauigkeit[m]",
            "age": "Alter in Jahren",
            "lon": "Längengrad [°]",
            "lat": "Breitengrad [°]"
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'is_collector')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_collector')