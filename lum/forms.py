from django import forms

class PubMedForm(forms.Form):
    """
    Slightly different if displayed in in-app browser (no captcha)
    """
    keywords = forms.CharField(label="Keywords", max_length=100)
