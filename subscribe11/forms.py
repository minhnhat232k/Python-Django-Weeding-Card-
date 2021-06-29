from django import forms
from .models import Subscribe11

class Subscribe11(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe11
        fields = "__all__"