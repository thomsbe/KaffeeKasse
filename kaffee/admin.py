from django.contrib import admin

from .models import AbrechnungsWoche, KaffeeKonfiguration, KontoBewegung, NutzerProfil

# Register your models here.

@admin.register(KaffeeKonfiguration)
class KaffeeKonfigurationAdmin(admin.ModelAdmin):
    list_display = ("preis_pro_kg", "gramm_pro_tasse", "gueltig_ab", "ist_aktiv")
    list_filter = ("ist_aktiv",)
    search_fields = ("gueltig_ab",)

@admin.register(KontoBewegung)
class KontoBewegungAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "datum", "typ", "menge_gramm", "wert_euro", "beschreibung", "mahlvorgaenge")
    list_filter = ("typ", "datum")
    search_fields = ("nutzer__username", "beschreibung")

@admin.register(NutzerProfil)
class NutzerProfilAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "tage_pro_woche", "kaffee_pro_tag", "mahlvorgaenge_pro_kaffee")
    search_fields = ("nutzer__username",)

@admin.register(AbrechnungsWoche)
class AbrechnungsWocheAdmin(admin.ModelAdmin):
    list_display = ("start_datum", "end_datum", "abgeschlossen")
    list_filter = ("abgeschlossen",)
