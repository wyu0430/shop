from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginForm(forms.ModelForm):
    '''
    用户登录表单

    '''
    username = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('password',)
        widgets = {
            'password': forms.PasswordInput()
        }


class UserRegForm(forms.ModelForm):
    '''
    用户注册表单
    '''
    class Meta:
        model = User
        fields = ('username',"password",'email')
        widgets = {
            'password': forms.PasswordInput()
        }