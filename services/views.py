from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Service
from .forms import QuoteForm, ContactForm


def home(request):
    services = Service.objects.filter(active=True)
    return render(request, 'home.html', {'services': services})


def quote(request):
    selected_service = None
    service_id = request.GET.get('service')

    if service_id:
        selected_service = Service.objects.filter(
            pk=service_id,
            active=True
        ).first()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Votre demande de devis a bien été envoyée. Nous vous contacterons prochainement.'
            )
            return redirect('quote')
    else:
        initial = {}

        if selected_service:
            initial['service'] = selected_service

        form = QuoteForm(initial=initial)

    return render(
        request,
        'quote.html',
        {
            'form': form,
            'selected_service': selected_service
        }
    )


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Votre message a bien été envoyé. Nous vous répondrons dans les meilleurs délais.'
            )
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def detail(request, pk):
    service = get_object_or_404(
        Service,
        pk=pk,
        active=True
    )

    return render(
        request,
        'service_detail.html',
        {'service': service}
    )
