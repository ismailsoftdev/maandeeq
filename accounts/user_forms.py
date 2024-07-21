from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the username'}), label='Username')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the first name'}), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the last name'}), label='Last Name')
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the password'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the confirm password'}), label='Confirm Password')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'groups', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'groups', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

