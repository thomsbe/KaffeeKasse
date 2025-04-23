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

class KontoBewegung(models.Model):
    TYP_CHOICES = [
        ("KAFFEE", "Kaffeebohnen"),
        ("GELD", "Geld"),
        ("SONSTIGES", "Sonstiges/Zubehör"),
        ("KONSUM", "Kaffeekonsum"),
    ]
    nutzer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="kontobewegungen")
    datum = models.DateField(auto_now_add=True)
    typ = models.CharField(max_length=16, choices=TYP_CHOICES)
    menge_gramm = models.PositiveIntegerField(null=True, blank=True, help_text="Nur für Kaffeebohnen/Konsum")
    wert_euro = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, help_text="Nur für Geld/Sonstiges")
    beschreibung = models.CharField(max_length=200, blank=True, help_text="z.B. Milch, Entkalker, Zubehör, Kommentar")
    mahlvorgaenge = models.PositiveIntegerField(null=True, blank=True, help_text="Nur für Konsum – wie oft gemahlen?")
    saldo_wert = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'), help_text="Wert, mit dem diese Bewegung den Kontostand beeinflusst (positiv/negativ)")
    ist_markiert = models.BooleanField(default=False, help_text="Vom Nutzer als unzutreffend markiert")
    markierungsgrund = models.CharField(max_length=255, blank=True, help_text="Grund/Bemerkung für die Markierung")

    def save(self, *args, **kwargs):
        # Berechne saldo_wert je nach Typ
        if self.typ == "GELD":
            self.saldo_wert = self.wert_euro or Decimal('0.00')
        elif self.typ == "KAFFEE":
            # Optional: Umrechnung Kaffeebohnen zu Euro, falls wert_euro gesetzt, sonst 0
            self.saldo_wert = self.wert_euro or Decimal('0.00')
        elif self.typ == "KONSUM":
            # Konsum ist immer negativ (z.B. -wert_euro)
            self.saldo_wert = -(self.wert_euro or Decimal('0.00'))
        elif self.typ == "SONSTIGES":
            self.saldo_wert = self.wert_euro or Decimal('0.00')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_typ_display()} durch {self.nutzer} am {self.datum}"

    class Meta:
        verbose_name = "Konto-Bewegung"
        verbose_name_plural = "Konto-Bewegungen"

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
