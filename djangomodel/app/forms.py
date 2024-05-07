from django import forms
g=[['male','Male'],['Female','Female']]
c=[['Python','Python'],['Java','Java'],['Testing','Testing']]

class ModelRegisterForm(forms.Form):
    name=forms.CharField(max_length=10, required=False)
    pno=forms.CharField( max_length=10, required=False)
    email=forms.EmailField(required=False)
    gender =forms.ChoiceField(choices=g, required=False,widget=forms.RadioSelect)
    course =forms.MultipleChoiceField(choices=c, required=False,widget=forms.CheckboxSelectMultiple)
    username=forms.CharField(max_length=20, required=False)
    password=forms.CharField(max_length=20, required=False,widget=forms.PasswordInput)
    
    