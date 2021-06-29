from django import forms
from .models import Subscribe9

class Subscribe9(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe9
        fields = "__all__"