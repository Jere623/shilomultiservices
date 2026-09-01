from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from services.models import Service


class StaticViewSitemap(Sitemap):

    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "quote",
            "contact",
        ]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):

    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return Service.objects.filter(
            active=True
        )

    def location(self, obj):
        return reverse(
            "detail",
            kwargs={
                "pk": obj.pk
            }
        )