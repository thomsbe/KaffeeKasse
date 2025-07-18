# Generated by Django 5.2 on 2025-04-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaffee', '0003_kontobewegung_saldo_wert'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontobewegung',
            name='ist_markiert',
            field=models.BooleanField(default=False, help_text='Vom Nutzer als unzutreffend markiert'),
        ),
        migrations.AddField(
            model_name='kontobewegung',
            name='markierungsgrund',
            field=models.CharField(blank=True, help_text='Grund/Bemerkung für die Markierung', max_length=255),
        ),
    ]
