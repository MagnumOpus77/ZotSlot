from django import forms

class CreateNewUser(forms.Form):
    name = forms.CharField(label="Username", max_length=8)
    #check = forms.BooleanField(required=False)
