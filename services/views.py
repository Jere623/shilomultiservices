from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from .models import Service
from .forms import QuoteForm, ContactForm


def home(request):
    services = Service.objects.filter(active=True)
    return render(
        request,
        "home.html",
        {"services": services}
    )


def quote(request):
    service_id = request.GET.get("service")

    initial = {}

    if service_id:
        try:
            service = Service.objects.get(
                pk=service_id,
                active=True
            )
            initial["service"] = service
        except Service.DoesNotExist:
            pass

    form = QuoteForm(
        request.POST or None,
        initial=initial
    )

    if request.method == "POST" and form.is_valid():

        quote_request = form.save()

        service_name = (
            quote_request.service.name
            if quote_request.service
            else "Service non précisé"
        )

        email_subject = (
            f"Nouvelle demande de devis - {service_name}"
        )

        email_message = f"""
Nouvelle demande de devis

Nom : {quote_request.name}
E-mail : {quote_request.email}
Téléphone : {quote_request.phone}
Service : {service_name}
Adresse : {quote_request.address}
Date souhaitée : {quote_request.preferred_date}

Message :
{quote_request.message}
"""

        try:
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                "Votre demande de devis a bien été envoyée."
            )

        except Exception:
            messages.warning(
                request,
                "Votre demande a été enregistrée. "
                "L'envoi de l'e-mail sera traité ultérieurement."
            )

        return redirect("quote")

    return render(
        request,
        "quote.html",
        {"form": form}
    )


def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        contact_message = form.save()

        email_subject = (
            f"Nouveau message de contact - "
            f"{contact_message.name}"
        )

        email_message = f"""
Nouveau message de contact

Nom : {contact_message.name}
E-mail : {contact_message.email}

Message :

{contact_message.message}
"""

        try:
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                "Votre message a bien été envoyé."
            )

        except Exception:
            messages.warning(
                request,
                "Votre message a été enregistré."
            )

        return redirect("contact")

    return render(
        request,
        "contact.html",
        {"form": form}
    )


def detail(request, pk):
    service = get_object_or_404(
        Service,
        pk=pk,
        active=True
    )

    return render(
        request,
        "service_detail.html",
        {"service": service}
    )
