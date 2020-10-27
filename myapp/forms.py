from django import forms

from .models import Person, Person_detail

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email', 'location')




class Person_detailForm(forms.ModelForm):
    class Meta:
        model = Person_detail
        fields = ('address', 'birth_date', 'phone','person_id','occupation')

