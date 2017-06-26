from django import forms


class NumberForm(forms.Form):
    your_name = forms.CharField()
    your_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
