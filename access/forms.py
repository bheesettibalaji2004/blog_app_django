from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posts

class CreatePostForm(forms.ModelForm):
    heading = forms.CharField(label="Heading",widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    sub_heading = forms.CharField(label="Sub heading",widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    description = forms.CharField(label="Description",widget=forms.Textarea(attrs={"class":"form-control","rows":2}))
    image = forms.ImageField()
    class Meta:
        model = Posts
        fields = ["heading","sub_heading","description","image"]
        
class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))
    
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2"]
