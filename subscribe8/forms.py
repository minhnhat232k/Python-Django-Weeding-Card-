from django import forms
from .models import Subscribe8

class Subscribe8(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe8
        fields = "__all__"