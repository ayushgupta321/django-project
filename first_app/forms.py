from django import forms
from .models import User

class newUser(forms.ModelForm):
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'test'}))
    class Meta():
        model = User
        fields= '__all__'
        