from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse

from services.views import home, quote, contact, detail
from services.sitemaps import ServiceSitemap, StaticViewSitemap
from django.http import HttpResponse

sitemaps = {
    "static": StaticViewSitemap,
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

    path(
        "robots.txt",
        lambda request: HttpResponse(
            "User-agent: *\n"
            "Allow: /\n"
            "Disallow: /admin/\n"
            "Sitemap: https://shilomultiservices.com/sitemap.xml\n",
            content_type="text/plain",
        ),
        name="robots_txt",
    ),
]