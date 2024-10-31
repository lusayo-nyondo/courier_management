from django.forms.renderers import DjangoTemplates

class FormRenderer(DjangoTemplates):
    form_template_name = 'dashboard/forms/form.html'
    formset_template_name = 'dashboard/forms/formset.html'
    field_template_name = 'dashboard/forms/field.html'
