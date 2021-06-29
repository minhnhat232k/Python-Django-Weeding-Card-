from django import forms
from .models import Subscribe10

class Subscribe10(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe10
        fields = "__all__"