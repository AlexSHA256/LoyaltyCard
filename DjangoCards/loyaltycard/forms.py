
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name')
    quantity = forms.IntegerField()
    date_act = forms.DateTimeField()

