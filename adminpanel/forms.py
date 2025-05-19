from django import forms
from .models import CustomUser ,Source

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'is_active', 'is_staff']

class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-purple-600',
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'is_active', 'is_staff']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-purple-600',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-purple-600',
            }),
            'role': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-purple-600',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300 rounded',
            }),
            'is_staff': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300 rounded',
            }),
        }

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['name', 'url']