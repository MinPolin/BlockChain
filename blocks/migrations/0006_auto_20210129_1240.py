# Generated by Django 3.0.4 on 2021-01-29 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0005_auto_20210128_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ['-height']},
        ),
    ]
