from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Service
from .forms import QuoteForm, ContactForm


def home(request):
    services = Service.objects.filter(active=True)
    return render(request, "home.html", {"services": services})


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
        form.save()

        messages.success(
            request,
            "Votre demande de devis a bien été envoyée."
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
        form.save()

        messages.success(
            request,
            "Votre message a bien été envoyé."
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
