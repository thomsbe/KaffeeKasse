from django.contrib import admin

from .models import (
    AbrechnungsWoche,
    Auszahlung,
    GeldEinzahlung,
    KaffeeEinlage,
    KaffeeKonfiguration,
    NutzerProfil,
    Transaktion,
    Wochenverbrauch,
)

# Register your models here.

@admin.register(KaffeeKonfiguration)
class KaffeeKonfigurationAdmin(admin.ModelAdmin):
    list_display = ("preis_pro_kg", "gramm_pro_tasse", "gueltig_ab", "ist_aktiv")
    list_filter = ("ist_aktiv",)
    search_fields = ("gueltig_ab",)

@admin.register(Transaktion)
class TransaktionAdmin(admin.ModelAdmin):
    list_display = ("typ", "nutzer", "datum", "saldo_wert", "beschreibung")
    list_filter = ("typ", "datum")
    search_fields = ("nutzer__username", "beschreibung")

@admin.register(KaffeeEinlage)
class KaffeeEinlageAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "datum", "saldo_wert", "menge_kg")
    search_fields = ("nutzer__username",)

@admin.register(GeldEinzahlung)
class GeldEinzahlungAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "datum", "saldo_wert", "zahlungsreferenz")
    search_fields = ("nutzer__username",)

@admin.register(Wochenverbrauch)
class WochenverbrauchAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "datum", "saldo_wert", "start_datum", "end_datum")
    search_fields = ("nutzer__username",)

@admin.register(Auszahlung)
class AuszahlungAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "datum", "saldo_wert", "bank_referenz")
    search_fields = ("nutzer__username",)

@admin.register(NutzerProfil)
class NutzerProfilAdmin(admin.ModelAdmin):
    list_display = ("nutzer", "tage_pro_woche", "kaffee_pro_tag", "mahlvorgaenge_pro_kaffee")
    search_fields = ("nutzer__username",)

@admin.register(AbrechnungsWoche)
class AbrechnungsWocheAdmin(admin.ModelAdmin):
    list_display = ("start_datum", "end_datum", "abgeschlossen")
    list_filter = ("abgeschlossen",)
