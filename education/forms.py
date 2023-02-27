from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator


class AddEducation(forms.Form):

    choices = [("BAC","Bac"),
        ("LICENCE_1","Bac +1"),
        ("LICENCE_2","Bac +2"),
        ("LICENCE_3","Bac +3"),
        ("MASTER_1","Bac +4"),
        ("MASTER2_2","Bac +5"),
        ("PhD","Doctorat")]
    title=forms.CharField(max_length=100)
    level= forms.ChoiceField(choices=choices)
    year=forms.IntegerField(validators=[MaxValueValidator(2023),MinValueValidator(1900)]
    )