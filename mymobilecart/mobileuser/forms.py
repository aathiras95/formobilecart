from django import forms
from mobileuser.models import MobileProducts
from django.contrib.auth.models import User
from django .contrib.auth.forms import UserCreationForm


class ProductDetailsAddForm(forms.ModelForm):
    # ProductCode=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # ProductName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # ProductRam = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # ProductDisplay=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # ProductCamera = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # ProductBattery = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # ProductPrice = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # ProductOfferPrice = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # ProductProcessor=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # ProductWarrenty=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # ProductSpecification=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=MobileProducts
        fields="__all__"

        widgets={
            'pro_cat':forms.TextInput(attrs={'class':'form-control'}),
            'pro_code':forms.TextInput(attrs={'class':'form-control'}),
            'pro_name':forms.TextInput(attrs={'class':'form-control'}),
            'pro_ram':forms.TextInput(attrs={'class':'form-control'}),
            'pro_dis':forms.TextInput(attrs={'class':'form-control'}),
            'pro_camera':forms.TextInput(attrs={'class':'form-control'}),
            'pro_battery':forms.TextInput(attrs={'class':'form-control'}),
            'pro_price':forms.NumberInput(attrs={'class':'form-control'}),
            'pro_offprice':forms.NumberInput(attrs={'class':'form-control'}),
            'pro_processor':forms.TextInput(attrs={'class':'form-control'}),
            'pro_warrenty':forms.TextInput(attrs={'class':'form-control'}),
            'pro_specification':forms.TextInput(attrs={'class':'form-control'})

        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'

        ]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
