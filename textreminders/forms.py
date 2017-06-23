from django import forms


class NumberForm(forms.Form):
    your_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                   error_messages="Phone number must be entered in the format: '+999999999'.")
