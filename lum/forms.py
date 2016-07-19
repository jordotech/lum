from django import forms

class PubMedForm(forms.Form):
    """
    Slightly different if displayed in in-app browser (no captcha)
    """
    q = forms.CharField(
        label="Keywords",
        max_length=100,
        widget=forms.TextInput(
            attrs={
        'placeholder':'Search',
                'class': 'form-control'
        })
    )
