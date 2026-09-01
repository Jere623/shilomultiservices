from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from services import views
from .sitemaps import StaticViewSitemap, ServiceSitemap


sitemaps = {
    "static": StaticViewSitemap,
    "services": ServiceSitemap,
}


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "devis/",
        views.quote,
        name="quote"
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),

    path(
        "services/<int:pk>/",
        views.detail,
        name="detail"
    ),

    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": sitemaps
        },
        name="django-sitemap"
    ),

    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
        name="robots"
    ),
]
