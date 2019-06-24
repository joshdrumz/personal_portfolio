from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter your name...'
        }
    ))
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'name@example.com'
        }
    ))
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Write a subject...'
        }
    ))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control form-control-sm',
            'rows': '8'
        }
    ))
