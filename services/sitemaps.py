from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Service


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return ["home", "contact", "quote"]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Service.objects.filter(active=True)

    def location(self, obj):
        return f"/services/{obj.pk}/"