from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import KontoBewegung

# --- Beispiel-Form für KontoBewegung (muss später angepasst werden) ---
class KontoBewegungForm(forms.ModelForm):
    class Meta:
        model = KontoBewegung
        fields = ["typ", "menge_gramm", "wert_euro", "beschreibung", "mahlvorgaenge"]
        widgets = {
            "typ": forms.Select(attrs={"class": "select select-bordered w-full"}),
            "menge_gramm": forms.NumberInput(attrs={"class": "input input-bordered w-full", "placeholder": "z.B. 500"}),
            "wert_euro": forms.NumberInput(attrs={"class": "input input-bordered w-full", "placeholder": "z.B. 4.50", "step": "0.01"}),
            "beschreibung": forms.TextInput(attrs={"class": "input input-bordered w-full", "placeholder": "Optionaler Kommentar"}),
            "mahlvorgaenge": forms.NumberInput(attrs={"class": "input input-bordered w-full", "placeholder": "z.B. 2"}),
        }

# Views

@login_required
def index(request):
    kontostand = KontoBewegung.objects.filter(nutzer=request.user).aggregate(Summe=Sum("saldo_wert"))["Summe"] or 0
    return render(request, "kaffee/index.html", {"kontostand": kontostand})

def statistiken(request):
    return render(request, "kaffee/statistiken.html")

@login_required
def profil(request):
    return render(request, "kaffee/profil.html")

@login_required
def kontoauszug(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    bewegungen = KontoBewegung.objects.filter(nutzer=request.user).order_by("-datum")
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

# Dummy-View für Einlage (muss später an KontoBewegung angepasst werden)
@login_required
def einlage(request):
    if request.method == "POST" and getattr(request, "htmx", False):
        form = KontoBewegungForm(request.POST)
        if form.is_valid():
            bewegung = form.save(commit=False)
            bewegung.nutzer = request.user
            bewegung.save()
            messages.success(request, "Eintrag erfolgreich eingetragen!")
            return render(request, "kaffee/partials/einlage_success.html", {"einlage": bewegung, "form": KontoBewegungForm()})
        else:
            return render(request, "kaffee/partials/einlage_form.html", {"form": form})
    else:
        form = KontoBewegungForm()
    return render(request, "kaffee/einlage.html", {"form": form})

@login_required
def konsum(request):
    return render(request, "kaffee/konsum.html")

@login_required
def markiere_bewegung_modal(request, bewegung_id):
    bewegung = get_object_or_404(KontoBewegung, id=bewegung_id, nutzer=request.user)
    return render(request, "kaffee/partials/markiere_bewegung_modal.html", {"bewegung": bewegung})

@require_POST
@login_required
def markiere_bewegung(request, bewegung_id):
    bewegung = get_object_or_404(KontoBewegung, id=bewegung_id, nutzer=request.user)
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
    bewegung = get_object_or_404(KontoBewegung, id=bewegung_id, nutzer=request.user)
    bewegung.ist_markiert = False
    bewegung.markierungsgrund = ""
    bewegung.save()
    # Nach dem Entfernen: Button zum Markieren anzeigen
    return render(request, "kaffee/partials/markierung_button.html", {"bewegung": bewegung})

def dashboard(request):
    return render(request, "kaffee/dashboard.html")
