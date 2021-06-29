from django import forms
from .models import Subscribe3

class Subscribe3(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe3
        fields = "__all__"