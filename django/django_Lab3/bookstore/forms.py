
from django import forms
from bookstore.models import AuthorModel, BookModel

class AuthorModelForm(forms.ModelForm):
    
    class Meta:
        model= AuthorModel
        fields='__all__'

class BookModelForm(forms.ModelForm):
    
    class Meta:
        model= BookModel
        fields='__all__'

    # def clean_email(self):
    #     """ when you raise error
    #     if the email already exists in another instance not in current instance

    #     self ==> modelform
    #     in case of create instance--> email ==> null

    #     if case of edit instance --> already created instance.email != email


    #     """
    #     email= self.cleaned_data['email']

    #     if (Student.objects.filter(email=email).exists()
    #             and self.instance.email!=email):
    #         raise forms.ValidationError("Email already exists")

    #     return email


    # def clean_name(self):
    #     name= self.cleaned_data['name']
    #     if len(name) < 2:
    #          raise forms.ValidationError("Name must be at least 2 characters ")
    #     return name

    # ## override save function
    # # def save(self, commit=True):
    # #     pass
