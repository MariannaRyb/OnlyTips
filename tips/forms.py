from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import WaiterProfile, CustomerProfile, Join, Transaction

class ExtendedRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={'class':'signup-form'}))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length = 150)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(ExtendedRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['password1'].TextInput = None

    def save(self, commit=True):
        user = super().save(commit = False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user



class WaiterProfileForm(ModelForm):
    class Meta:
        model = WaiterProfile
        fields = ('wallet', 'description', 'image', 'cafe')




class CustomerProfileForm(ModelForm):
    class Meta:
        model = CustomerProfile
        fields=['wallet', 'image']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    #def __init__(self, *args, **kwargs):
        #super(UserUpdateForm, self).__init__(*args, **kwargs)
        #self.fields['username'].help_text = None


class WaiterUpdateForm(ModelForm):
    class Meta:
        model=WaiterProfile
        fields=('wallet', 'description', 'image', 'cafe')

class CustomerUpdateForm(ModelForm):
    class Meta:
        model=CustomerProfile
        fields=('wallet', 'image')


class JoinForm(ModelForm):
    class Meta:
        model = Join
        fields = '__all__'


class TokenTransactForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'comment']




