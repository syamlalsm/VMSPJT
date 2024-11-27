from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'age', 'gender', 'place', 'photo', 'visit_time', 'purpose', 'visit_date', 'email', 'phone_number']

  
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise forms.ValidationError("Phone number must be 10 digits.")
        return phone_number
