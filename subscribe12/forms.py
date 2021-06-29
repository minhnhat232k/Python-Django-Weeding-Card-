from django import forms
from .models import Subscribe12

class Subscribe12(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe12
        fields = "__all__"