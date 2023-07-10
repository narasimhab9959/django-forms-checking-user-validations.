from django import forms

def validate_of_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError('Error')


def validate_of_length(name):
    if len(name)<=5:
        raise forms.ValidationError('less than 5')

class studentform(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_of_a])
    sage=forms.IntegerField()
    semail=forms.EmailField(max_length=100)