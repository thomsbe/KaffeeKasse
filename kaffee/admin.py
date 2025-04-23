from django.contrib import admin
from .models import KaffeeKonfiguration, Einlage, Konsum, NutzerProfil

# Register your models here.

@admin.register(KaffeeKonfiguration)
class KaffeeKonfigurationAdmin(admin.ModelAdmin):
    list_display = ("preis_pro_kg", "gramm_pro_tasse", "gueltig_ab", "ist_aktiv")
    list_filter = ("ist_aktiv",)
    search_fields = ("preis_pro_kg", "gramm_pro_tasse")

@admin.register(Einlage)
class EinlageAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "datum", "menge_gramm", "wert_euro", "kommentar")
    list_filter = ("datum",)
    search_fields = ("nutzer__username", "kommentar")

@admin.register(Konsum)
class KonsumAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "datum", "anzahl_tassen", "mahlvorgaenge", "kommentar")
    list_filter = ("datum",)
    search_fields = ("nutzer__username", "kommentar")

@admin.register(NutzerProfil)
class NutzerProfilAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "bevorzugte_mahlart", "durchschnitt_tassen_pro_woche")
    search_fields = ("nutzer__username", "bevorzugte_mahlart")
