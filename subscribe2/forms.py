from django import forms
from .models import Subscribe2

class Subscribe2(forms.ModelForm):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
    class Meta:  
        model = Subscribe2  
        fields = "__all__"  