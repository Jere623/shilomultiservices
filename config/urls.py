from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from services.sitemaps import ServiceSitemap


sitemaps = {
    'services': ServiceSitemap,
}


urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='sitemap'
    ),

    path(
        '',
        include('services.urls')
    ),
]
