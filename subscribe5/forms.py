from django import forms
from .models import Subscribe5

class Subscribe2(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe5
        fields = "__all__"