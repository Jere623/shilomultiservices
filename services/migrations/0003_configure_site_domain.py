from django.db import migrations


def configure_site_domain(apps, schema_editor):
    Site = apps.get_model("sites", "Site")

    Site.objects.update_or_create(
        id=1,
        defaults={
            "domain": "shilomultiservices.com",
            "name": "Shilo Multi-Services",
        },
    )


def reverse_configure_site_domain(apps, schema_editor):
    Site = apps.get_model("sites", "Site")

    Site.objects.filter(id=1).update(
        domain="example.com",
        name="example.com",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("services", "0002_service_benefits_service_frequency_and_more"),
    ]

    operations = [
        migrations.RunPython(
            configure_site_domain,
            reverse_configure_site_domain,
        ),
    ]