from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()



class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['nickname', 'avatar', 'bio']



class RegistrationForm(forms.ModelForm):
    password_1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )
    
    class Meta:
        model = User
        fields = ['username', 'nickname', 'avatar', 'bio']
    
    def clean(self):
        cleaned_data = super().clean()
        password_1 = cleaned_data.get("password_1")
        password_2 = cleaned_data.get("password_2")
        
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150
    )
    password = forms.CharField(
        widget=forms.PasswordInput
    )





