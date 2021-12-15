from django import forms

HANDY_SERVICES = [
    ("Construction", "Construction"),
    ("Mechanic", "Mechanic"),
    ("Logistic", "Logistic"),
    ("Webb", "Webb"),
    ("Law", "Law"),
    ("Other", "Other"),
]


class ContactForm(forms.Form):
    """ Form for contact page - Send_mail """

    name = forms.CharField(required=True, max_length=90)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=40)
    handyService = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=HANDY_SERVICES,
        label="Service Selection",
    )
    message = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"rows": 4}))
