from django import forms

from .models import Money, Budget

class moneyForm(forms.ModelForm):
    class Meta:
        model = Money
        exclude = ["owner"]
                
class budgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        exclude = ["owner"]