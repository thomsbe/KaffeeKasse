from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

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

class Einlage(models.Model):
    nutzer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="einlagen")
    datum = models.DateField(auto_now_add=True)
    menge_gramm = models.PositiveIntegerField(help_text="Menge in Gramm")
    wert_euro = models.DecimalField(max_digits=7, decimal_places=2, help_text="Wert in Euro")
    kommentar = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nutzer} - {self.menge_gramm}g für {self.wert_euro}€ am {self.datum}"

    class Meta:
        verbose_name = "Einlage"
        verbose_name_plural = "Einlagen"

class Konsum(models.Model):
    nutzer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="konsume")
    datum = models.DateField(auto_now_add=True)
    anzahl_tassen = models.PositiveIntegerField(default=1)
    mahlvorgaenge = models.PositiveIntegerField(default=1, help_text="Wie oft wurde gemahlen?")
    kommentar = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nutzer} - {self.anzahl_tassen} Tassen ({self.mahlvorgaenge}x) am {self.datum}"

    class Meta:
        verbose_name = "Konsum"
        verbose_name_plural = "Konsume"

class NutzerProfil(models.Model):
    nutzer = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profil")
    bevorzugte_mahlart = models.CharField(max_length=100, blank=True)
    durchschnitt_tassen_pro_woche = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Profil von {self.nutzer}"

    class Meta:
        verbose_name = "Nutzerprofil"
        verbose_name_plural = "Nutzerprofile"
