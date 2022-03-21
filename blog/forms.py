from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Text message', widget=forms.Textarea(attrs={'class': 'form-control'}))    