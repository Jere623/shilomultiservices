from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Service
from .forms import QuoteForm,ContactForm
def home(request): return render(request,'home.html',{'services':Service.objects.filter(active=True)})
def quote(request):
    form=QuoteForm(request.POST or None)
    if request.method=='POST' and form.is_valid(): form.save(); messages.success(request,'Votre demande de devis a bien été envoyée.'); return redirect('quote')
    return render(request,'quote.html',{'form':form})
def contact(request):
    form=ContactForm(request.POST or None)
    if request.method=='POST' and form.is_valid(): form.save(); messages.success(request,'Votre message a bien été envoyé.'); return redirect('contact')
    return render(request,'contact.html',{'form':form})
def detail(request,pk): return render(request,'service_detail.html',{'service':get_object_or_404(Service,pk=pk,active=True)})
