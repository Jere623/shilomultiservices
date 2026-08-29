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

/* =========================================
   PHASE 3 - PAGE SERVICE
========================================= */

.service-page {
    max-width: 1180px;
    margin: 0 auto;
    padding: 80px 30px 100px;
}

/* En-tête */

.service-header {
    max-width: 850px;
    margin: 0 auto 70px;
    text-align: center;
}

.service-header h1 {
    font-size: clamp(42px, 6vw, 68px);
    line-height: 1.08;
    margin: 15px 0 25px;
}

.service-intro {
    max-width: 720px;
    margin: 0 auto;
    font-size: 20px;
    line-height: 1.7;
    color: #66736b;
}


/* Contenu principal */

.service-layout {
    display: grid;
    grid-template-columns: minmax(0, 1.7fr) minmax(280px, 0.8fr);
    gap: 70px;
    align-items: start;
}

.service-main {
    min-width: 0;
}

.service-main h2 {
    font-size: 36px;
    line-height: 1.2;
    margin: 0 0 30px;
}

.service-description {
    font-size: 17px;
    line-height: 1.85;
    color: #4f5d55;
}

.service-description p {
    margin: 0 0 22px;
}


/* Carte latérale */

.service-sidebar {
    min-width: 0;
}

.service-card {
    background: #f7f4ec;
    border: 1px solid #e8e1d2;
    border-radius: 18px;
    padding: 32px;
}

.service-card h3 {
    font-size: 23px;
    line-height: 1.3;
    margin: 8px 0 25px;
}

.service-card ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.service-card li {
    position: relative;
    padding-left: 25px;
    margin-bottom: 17px;
    color: #4f5d55;
    line-height: 1.5;
}

.service-card li::before {
    content: "✓";
    position: absolute;
    left: 0;
    color: var(--green);
    font-weight: bold;
}


/* Appel à l'action */

.service-cta {
    margin-top: 80px;
    padding: 55px 60px;
    border-radius: 22px;
    background: var(--dark);
    color: white;

    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 50px;
}

.service-cta > div {
    max-width: 680px;
}

.service-cta .eyebrow {
    color: var(--gold);
}

.service-cta h2 {
    font-size: 38px;
    line-height: 1.15;
    margin: 10px 0 15px;
}

.service-cta p:not(.eyebrow) {
    color: #dbe3dd;
    font-size: 17px;
    line-height: 1.7;
    margin: 0;
}


/* Mobile */

@media (max-width: 800px) {

    .service-page {
        padding: 60px 22px 75px;
    }

    .service-header {
        margin-bottom: 50px;
    }

    .service-header h1 {
        font-size: 42px;
    }

    .service-intro {
        font-size: 18px;
    }

    .service-layout {
        grid-template-columns: 1fr;
        gap: 40px;
    }

    .service-main h2 {
        font-size: 30px;
    }

    .service-cta {
        margin-top: 55px;
        padding: 40px 30px;
        flex-direction: column;
        align-items: flex-start;
        gap: 30px;
    }

    .service-cta h2 {
        font-size: 32px;
    }
}
