from django.contrib import admin

from .models import Service, QuoteRequest, ContactMessage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_description',
        'active',
    )

    list_filter = (
        'active',
    )

    search_fields = (
        'name',
        'short_description',
        'description',
    )

    ordering = (
        'name',
    )


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'service',
        'preferred_date',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'service',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'address',
        'message',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    list_per_page = 25


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'handled',
        'created_at',
    )

    list_filter = (
        'handled',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'message',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    list_per_page = 25
