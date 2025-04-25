from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Transaktion

# --- Beispiel-Form für Transaktion (muss später angepasst werden) ---
class TransaktionForm(forms.ModelForm):
    class Meta:
        model = Transaktion
        fields = ["typ", "saldo_wert", "beschreibung"]
        widgets = {
            "typ": forms.Select(attrs={"class": "select select-bordered w-full"}),
            "saldo_wert": forms.NumberInput(attrs={"class": "input input-bordered w-full", "placeholder": "z.B. 4.50", "step": "0.01"}),
            "beschreibung": forms.TextInput(attrs={"class": "input input-bordered w-full", "placeholder": "Optionaler Kommentar"}),
        }

# Views

def index(request):
    if request.user.is_authenticated:
        kontostand = Transaktion.objects.filter(nutzer=request.user).aggregate(Summe=Sum("saldo_wert"))["Summe"] or 0
        page = int(request.GET.get("page", 1))
        page_size = 10
        transaktionen = Transaktion.objects.filter(nutzer=request.user).order_by("-datum")
        paginator = Paginator(transaktionen, page_size)
        page_obj = paginator.get_page(page)
        has_next = page_obj.has_next()
        next_page = page + 1
        form = TransaktionForm()
        context = {
            "kontostand": kontostand,
            "page_obj": page_obj,
            "has_next": has_next,
            "next_page": next_page,
            "form": form,
        }
        return render(request, "kaffee/index.html", context)
    # Für nicht authentifizierte Nutzer
    return render(request, "kaffee/index.html")

def statistiken(request):
    return render(request, "kaffee/statistiken.html")

@login_required
def profil(request):
    return render(request, "kaffee/profil.html")

@login_required
def kontoauszug(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    bewegungen = Transaktion.objects.filter(nutzer=request.user).order_by("-datum")
    paginator = Paginator(bewegungen, page_size)
    page_obj = paginator.get_page(page)
    is_htmx = getattr(request, "htmx", False)
    template = "kaffee/partials/kontoauszug_liste.html" if is_htmx else "kaffee/profil.html"
    context = {
        "page_obj": page_obj,
        "has_next": page_obj.has_next(),
        "next_page": page + 1,
        "is_htmx": is_htmx,
    }
    return render(request, template, context)

# Dummy-View für Einlage (muss später an Transaktion angepasst werden)
@login_required
def einlage(request):
    if getattr(request, "htmx", False):
        if request.method == "GET":
            form = TransaktionForm()
            return render(request, "kaffee/partials/einlage_form.html", {"form": form})
        if request.method == "POST":
            form = TransaktionForm(request.POST)
            if form.is_valid():
                bewegung = form.save(commit=False)
                bewegung.nutzer = request.user
                bewegung.save()
                messages.success(request, "Eintrag erfolgreich eingetragen!")
                return render(request, "kaffee/partials/einlage_success.html", {"einlage": bewegung, "form": TransaktionForm()})
            else:
                return render(request, "kaffee/partials/einlage_form.html", {"form": form})
    # Non-HTMX fallback: full page
    form = TransaktionForm()
    return render(request, "kaffee/einlage.html", {"form": form})

@login_required
def konsum(request):
    return render(request, "kaffee/konsum.html")

@login_required
def markiere_bewegung_modal(request, bewegung_id):
    bewegung = get_object_or_404(Transaktion, id=bewegung_id, nutzer=request.user)
    return render(request, "kaffee/partials/markiere_bewegung_modal.html", {"bewegung": bewegung})

@require_POST
@login_required
def markiere_bewegung(request, bewegung_id):
    bewegung = get_object_or_404(Transaktion, id=bewegung_id, nutzer=request.user)
    if bewegung.ist_markiert:
        return render(request, "kaffee/partials/markiert_badge.html", {"bewegung": bewegung})
    grund = request.POST.get("grund", "")
    bewegung.ist_markiert = True
    bewegung.markierungsgrund = grund
    bewegung.save()
    return render(request, "kaffee/partials/markiert_badge.html", {"bewegung": bewegung})

@require_POST
@login_required
def entmarkiere_bewegung(request, bewegung_id):
    bewegung = get_object_or_404(Transaktion, id=bewegung_id, nutzer=request.user)
    bewegung.ist_markiert = False
    bewegung.markierungsgrund = ""
    bewegung.save()
    # Nach dem Entfernen: Button zum Markieren anzeigen
    return render(request, "kaffee/partials/markierung_button.html", {"bewegung": bewegung})

def dashboard(request):
    return render(request, "kaffee/dashboard.html")

def test_components(request):
    from datetime import datetime

    class DummyBewegung:
        def __init__(self, typ, typ_display, datum, beschreibung):
            self.typ = typ
            self._typ_display = typ_display
            self.datum = datum
            self.beschreibung = beschreibung

        @property
        def get_typ_display(self):
            return self._typ_display

    beispiel_transaktionen = [
        DummyBewegung('GELD', 'Geld-Einzahlung', datetime(2025, 4, 25, 11, 0), 'Einzahlung 10€'),
        DummyBewegung('KAFFEE', 'Kaffeebohnen-Einlage', datetime(2025, 4, 24, 9, 30), '1kg Bohnen'),
        DummyBewegung('WOCHENVERBRAUCH', 'Wochenverbrauch', datetime(2025, 4, 20, 12, 0), '5 Tassen'),
        DummyBewegung('AUSZAHLUNG', 'Auszahlung', datetime(2025, 4, 18, 14, 0), 'Rückzahlung'),
    ]
    context = {
        'page_obj': beispiel_transaktionen,
        'has_next': True,
        'next_page': 2,
        'single_bewegung': beispiel_transaktionen[0],
    }
    return render(request, "kaffee/test_components.html", context)
