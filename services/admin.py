from django.contrib import admin

from .models import Service, QuoteRequest, ContactMessage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "active",
    )

    list_filter = (
        "active",
    )

    search_fields = (
        "name",
        "short_description",
        "description",
    )

    ordering = (
        "id",
    )


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "service",
        "preferred_date",
    )

    list_filter = (
        "service",
        "preferred_date",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "address",
        "message",
    )

    readonly_fields = (
        "name",
        "email",
        "phone",
        "service",
        "address",
        "preferred_date",
        "message",
    )

    ordering = (
        "-id",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
    )

    search_fields = (
        "name",
        "email",
        "message",
    )

    readonly_fields = (
        "name",
        "email",
        "message",
    )

    ordering = (
        "-id",
    )
