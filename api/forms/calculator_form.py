from django import forms


class CalculationForm(forms.Form):
    expression = forms.CharField(label="Expression", max_length=100)
