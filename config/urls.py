from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap

from services.views import home, quote, contact, detail
from services.sitemaps import ServiceSitemap


sitemaps = {
    "services": ServiceSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("devis/", quote, name="quote"),
    path("contact/", contact, name="contact"),
    path("services/<int:pk>/", detail, name="detail"),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),
]
