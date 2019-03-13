from django import forms
from .models import User

class newUser(forms.ModelForm):
    email = forms.EmailField(label="Email")
    class Meta():
        model = User
        fields= '__all__'
        