from django import forms
from modelforms.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields="__all__"
        