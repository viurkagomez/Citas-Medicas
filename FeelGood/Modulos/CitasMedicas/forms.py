from django import forms

class AppointmentForm(forms.Form):
    cedula = forms.CharField(max_length=11)
    email = forms.EmailField()
    phone = forms.CharField(max_length=50)
    diacita = forms.DateField()
    especialidad = forms.CharField(max_length=10)
    doctor = forms.CharField(max_length=10)
    message = forms.CharField(widget=forms.Textarea)
