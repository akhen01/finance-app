from django import forms
from .models import *

class incomeT_registry(forms.ModelForm):
    class Meta:
        model = incometype
        fields = ['name']

class budgetT_registry(forms.ModelForm):
    class Meta:
        model = budgettype
        fields = ['name']

class income_registry(forms.ModelForm):
    class Meta:
        model = income
        fields = ["amount", "Itype"]


class budget_registry(forms.ModelForm):
    class Meta:
        model = budget
        fields = ["amount", "Itype"]

class today_expences_form(forms.ModelForm):
    class Meta:
        model = expence
        fields = ["amount", "Itype"]