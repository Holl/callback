from django import forms
from auditioneer.models import Audition, Part

__author__ = 'holl'


class AuditionForm(forms.ModelForm):



    class Meta(object):
        model = Audition
        fields = ["name", "description",
                  "picture", "location_name", "audition_date",
                  "tag", "latitude", "longitude"]

class PartForm(forms.ModelForm):

    class Meta(object):
        model = Part
        fields = ["name", "description",
                  "gender", "age_range",]