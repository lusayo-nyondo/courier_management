from django import forms

from .models import (
    Client
)

from dashboard.widgets import (
    TextInput
)

class ClientForm(forms.ModelForm):
    template_name_p = 'dashboard/form_widgets/p.html'
    
    full_name = forms.CharField(
        widget=TextInput
    )
    
    class Meta:
        model = Client
        fields = '__all__'