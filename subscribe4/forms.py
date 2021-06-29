from django import forms
from .models import Subscribe4

class Subscribe2(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:
        model = Subscribe4
        fields = "__all__"