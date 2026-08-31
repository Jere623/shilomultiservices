from django.contrib.sitemaps import Sitemap

from .models import Service


class ServiceSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Service.objects.filter(active=True)

    def location(self, obj):
        return f'/services/{obj.pk}/'