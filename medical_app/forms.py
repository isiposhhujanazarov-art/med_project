from django import forms
from .models import Vrachi, Hospital, Polyklinika, Patient, PoseheniePolik


class VrachiForm(forms.ModelForm):
    class Meta:
        model = Vrachi
        fields = ['fio', 'specialis', 'start_date', 'photo']
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name_org', 'addres', 'telephone', 'vrach', 'photo']


class PolyklinikaForm(forms.ModelForm):
    class Meta:
        model = Polyklinika
        fields = ['name', 'addres', 'telephone', 'vrach']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['fio', 'pol', 'data_rozh']
        widgets = {'data_rozh': forms.DateInput(attrs={'type': 'date'})}


class PoseheniePolikForm(forms.ModelForm):
    class Meta:
        model = PoseheniePolik
        fields = ['data_posesheniya', 'time', 'patient', 'polyklinika']
        widgets = {
            'data_posesheniya': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }