from django import forms


class ApplicationForm(forms.Form):
    # Here same code as db model but just for form
    # Names should be same in form.cleaned.
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
