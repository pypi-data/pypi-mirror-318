# Generated by Django 3.2.18 on 2023-04-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_htmlsitemap", "0002_auto_20180228_1210"),
    ]

    operations = [
        migrations.AlterField(
            model_name="htmlsitemappluginconf",
            name="in_navigation",
            field=models.BooleanField(
                default=None, null=True, verbose_name="In navigation"
            ),
        ),
    ]
