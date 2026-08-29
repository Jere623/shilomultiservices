from django import forms
from .models import QuoteRequest, ContactMessage


class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest

        fields = [
            'name',
            'email',
            'phone',
            'service',
            'address',
            'preferred_date',
            'message'
        ]

        labels = {
            'name': 'Nom et prénom',
            'email': 'Adresse e-mail',
            'phone': 'Numéro de téléphone',
            'service': 'Service souhaité',
            'address': "Adresse de l’intervention",
            'preferred_date': 'Date souhaitée',
            'message': 'Décrivez votre besoin'
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Votre nom et prénom'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'exemple@email.com'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Votre numéro de téléphone'
                }
            ),

            'address': forms.TextInput(
                attrs={
                    'placeholder': "Adresse ou ville de l’intervention"
                }
            ),

            'preferred_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'rows': 6,
                    'placeholder': 'Expliquez-nous votre besoin : surface, fréquence souhaitée, nombre de pièces, type de locaux, etc.'
                }
            )
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage

        fields = [
            'name',
            'email',
            'phone',
            'message'
        ]

        labels = {
            'name': 'Nom et prénom',
            'email': 'Adresse e-mail',
            'phone': 'Numéro de téléphone',
            'message': 'Votre message'
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Votre nom et prénom'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'exemple@email.com'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Votre numéro de téléphone'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'rows': 6,
                    'placeholder': 'Comment pouvons-nous vous aider ?'
                }
            )
        }
