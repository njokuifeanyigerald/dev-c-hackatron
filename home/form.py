from django import forms

TITLE_CHOICES =[
    ('py', 'pyladies'),
    ('dev c', 'hackatron'),
    ('dsc', 'dsc futo'),
]

class HomeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'name',
        'class': 'form-control text-capitalize'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'email',
        'class': 'form-control text-capitalize'
    }))
    number = forms.CharField(label="phone number",widget=forms.NumberInput(attrs={
        'placeholder': 'phone number',
        'class': 'form-control text-capitalize'
    }))
    event = forms.CharField(
        max_length=15, widget=forms.Select(choices=TITLE_CHOICES, attrs={
            'placeholder': 'select an event',
            'class': 'form-control text-capitalize',

        })
    )
    about_self = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'tell us about your skill set',
        'class': 'form-control text-capitalize',
        "rows": 2,
        "cols": 120
    }))

