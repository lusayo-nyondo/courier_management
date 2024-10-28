from django.forms.widgets import (
    TextInput as DefaultTextInput
)

class TextInput(DefaultTextInput):
    template_name = 'dashboard/form_widgets/text_input.html'