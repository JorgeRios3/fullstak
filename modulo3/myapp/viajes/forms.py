from django import forms

class NameForm(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100, error_messages={'required': 'Please enter your name'})
    apellido_paterno = forms.CharField(label='apellido paterno', max_length=100)
    apellido_materno = forms.CharField(label='apellido paterno', max_length=100)
    edad = forms.IntegerField(error_messages={"required":"jaja"})
