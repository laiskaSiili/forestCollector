from django.forms import ModelForm, Textarea
from .models import Person, Video, StandInformation

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

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
        fields= ["lat", "lon", "accuracy", "entwicklungsstufe", "mischungsgrad", "bemerkungen"]
        widgets = {
            'bemerkungen': Textarea(attrs={'rows': 3}),
        }
        labels = {
            "accuracy": "Genauigkeit[m]",
            "lon": "Längengrad",
            "lat": "Breitengrad"
        }