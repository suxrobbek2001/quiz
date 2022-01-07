from django import forms

from .models import Quiz, Savol


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['nom', 'batafsil', 'savol_son', 'davomiyligi']



class SavolForm(forms.ModelForm):
    class Meta:
        model = Savol
        fields = ['matn', 'quiz']