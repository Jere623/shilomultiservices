from django import forms
from .models import QuoteRequest,ContactMessage
class QuoteForm(forms.ModelForm):
    class Meta:
        model=QuoteRequest; fields=['name','email','phone','service','address','preferred_date','message']
        widgets={'preferred_date':forms.DateInput(attrs={'type':'date'}),'message':forms.Textarea(attrs={'rows':5})}
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactMessage; fields=['name','email','phone','message']; widgets={'message':forms.Textarea(attrs={'rows':5})}
