# Generated by Django 4.0.3 on 2022-03-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_plugin_author_plugin_entry_plugin_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugin',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='entry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]