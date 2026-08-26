from django.contrib import admin
from .models import Service,QuoteRequest,ContactMessage
admin.site.register(Service)
@admin.register(QuoteRequest)
class QuoteAdmin(admin.ModelAdmin): list_display=('created_at','name','phone','service','status'); list_filter=('status','service'); search_fields=('name','email','phone')
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin): list_display=('created_at','name','email','handled'); list_filter=('handled',); search_fields=('name','email')
