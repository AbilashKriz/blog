# from typing import Any
# from django import forms
# from django.core import validators

# def check_for_a(value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError('Name needs to start with A')


# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_a])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label="Enter the email againS")
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])
    
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']

#         if email != vmail:
#             raise forms.ValidationError("MAKE SURE THE EMAILS MATCH!!")

from django import forms
from djangoPartII.models import Friends

class NewUser(forms.ModelForm):
    class Meta:
        model = Friends
        fields = '__all__'