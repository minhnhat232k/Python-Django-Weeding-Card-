from django import forms
from .models import Subscribe

class Subscribe(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:  
        model = Subscribe  
        fields = "__all__"  