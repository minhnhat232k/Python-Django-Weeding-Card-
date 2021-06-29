from django import forms
from .models import Subscribe7

class Subscribe7(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe7
        fields = "__all__"