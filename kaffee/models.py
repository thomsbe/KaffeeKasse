from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models


class KaffeeKonfiguration(models.Model):
    preis_pro_kg = models.DecimalField(max_digits=6, decimal_places=2, help_text="Preis pro Kilogramm Bohnen in Euro")
    gramm_pro_tasse = models.DecimalField(max_digits=5, decimal_places=2, help_text="Durchschnittlicher Verbrauch pro Tasse in Gramm")
    gueltig_ab = models.DateField(help_text="Gültig ab Datum")
    ist_aktiv = models.BooleanField(default=True, help_text="Ist diese Konfiguration aktiv?")

    def __str__(self):
        return f"{self.preis_pro_kg} €/kg, {self.gramm_pro_tasse}g/Tasse ab {self.gueltig_ab} (aktiv: {self.ist_aktiv})"

    class Meta:
        verbose_name = "Kaffee-Konfiguration"
        verbose_name_plural = "Kaffee-Konfigurationen"


class Transaktion(models.Model):
    TYP_KAFFEE     = "KAFFEE"
    TYP_GELD       = "GELD"
    TYP_WOCHE      = "WOCHENVERBRAUCH"
    TYP_AUSZAHLUNG = "AUSZAHLUNG"
    TYP_CHOICES = [
        (TYP_KAFFEE,    "Kaffeebohnen-Einlage"),
        (TYP_GELD,      "Geld-Einzahlung"),
        (TYP_WOCHE,     "Wochenverbrauch"),
        (TYP_AUSZAHLUNG,"Auszahlung"),
    ]

    typ          = models.CharField(max_length=20, choices=TYP_CHOICES)
    nutzer       = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datum        = models.DateTimeField(auto_now_add=True)
    saldo_wert   = models.DecimalField(
                     max_digits=7,
                     decimal_places=2,
                     default=Decimal('0.00'),
                     help_text='Wert der Transaktion (positiv/negativ)'
                   )
    beschreibung = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Transaktion'
        verbose_name_plural = 'Transaktionen'


class KaffeeEinlage(Transaktion):
    menge_kg     = models.DecimalField(max_digits=6, decimal_places=2, help_text='Menge in kg')
    zusatz_info  = models.TextField(blank=True, help_text="z.B. '5x 1kg vom Aldi'")


class GeldEinzahlung(Transaktion):
    zahlungsreferenz = models.CharField(max_length=100, blank=True, help_text='z.B. PayPal-Transaktions-ID')


class Wochenverbrauch(Transaktion):
    start_datum = models.DateField()
    end_datum   = models.DateField()


class Auszahlung(Transaktion):
    bank_referenz = models.CharField(max_length=100, blank=True, help_text='z.B. IBAN oder Verwendungszweck')


class NutzerProfil(models.Model):
    nutzer = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profil")
    bevorzugte_mahlart = models.CharField(max_length=100, blank=True)
    durchschnitt_tassen_pro_woche = models.PositiveIntegerField(default=0)
    tage_pro_woche = models.PositiveIntegerField(default=0, help_text="Anzahl der Tage pro Woche im Büro")
    kaffee_pro_tag = models.PositiveIntegerField(default=1, help_text="Tassen Kaffee pro Tag")
    mahlvorgaenge_pro_kaffee = models.PositiveIntegerField(default=1, help_text="Wie oft wird pro Kaffee gemahlen?")

    def __str__(self):
        return f"Profil von {self.nutzer}"

    class Meta:
        verbose_name = "Nutzerprofil"
        verbose_name_plural = "Nutzerprofile"


class AbrechnungsWoche(models.Model):
    start_datum = models.DateField(help_text="Startdatum der Woche (Montag)")
    end_datum = models.DateField(help_text="Enddatum der Woche (Sonntag)")
    abgeschlossen = models.BooleanField(default=False, help_text="Wurde die Woche bereits abgerechnet?")

    def __str__(self):
        return f"Abrechnungswoche {self.start_datum} - {self.end_datum} ({'abgeschlossen' if self.abgeschlossen else 'offen'})"

    class Meta:
        verbose_name = "Abrechnungswoche"
        verbose_name_plural = "Abrechnungswochen"
