# Projektplan: KaffeeKasse

## Stand: 25.04.2025

---

## 1. Aktueller Stand

- **Öffentliche Startseite** (`/`):
  - Unangemeldete sehen Hero mit Projektbeschreibung und Login/Signup-Buttons.
  - Authentifizierte sehen Kontostand, Farbhinweis (Minus/Null/Plus), Button „Neue Transaktion“ und das HTMX-geladene Transaktionen-Listing.
- **Transaktionsmodell** `Transaktion` mit Unterklassen (`KaffeeEinlage`, `GeldEinzahlung`, `Wochenverbrauch`, `Auszahlung`) per Multi-Table Inheritance vollständig implementiert.
- **HTMX-Integration**:
  - Partial-Templates für Formular (`einlage_form.html`), Erfolgsmeldung (`einlage_success.html`) und Listing (`kontoauszug_liste.html`).
  - Paginierung mit HTMX-Infinite-Loading.
- **Allauth-Anpassungen**:
  - Login-Template im DaisyUI-Stil überschrieben.
  - Hidden-`next`-Input und `LOGIN_REDIRECT_URL = '/'` konfiguriert.
  - Redirect für `/accounts/profile/` auf Index hinzugefügt.
- **Technisches Setup**:
  - Django 5.1.7, Tailwind CSS v4, DaisyUI 5, django_htmx, django_browser_reload.
- **Refactoring & UI-Komponenten**:
  - Umstellung auf Cotton-Komponenten für alle zentralen UI-Elemente (Buttons, Formulare, Modals, Badges, Listen, Pagination)
  - DaisyUI v5 als Standard für Styles
  - HTMX für dynamische Formulare und UI
  - Alpine.js für Modal-Steuerung
  - Account-Templates (Login, Signup) auf Cotton/DaisyUI refaktorisiert
  - Alte Partials/Komponenten entfernt (siehe Liste unten)
  - Fehlerbehebungen: Button-Komponente robust, Modal steuerbar
  - Neue Cotton-Komponente: hero

---

## 2. Nächste Schritte

- **Weitere Allauth-Templates** anpassen (Passwort-Reset, E-Mail-Bestätigung).
- **Profil-Seite** (`/profil/`): Nutzerdetails, Kontoauszug-Link, evtl. Einstellungen.
- **Testing**:
  - Unit-Tests für Views, Formulare und Modelle.
  - Integrationstests für HTMX-Flows.
- **Error Handling & Logging**:
  - Logging von Transaktionen und Fehlern.
  - Nutzerfreundliche Fehlermeldungen.
- **UI/UX & Accessibility** prüfen und optimieren.
- **Deployment**:
  - Prod-Settings (Debug=False, Env-Variablen), collectstatic, Migrationen.
- **Best Practice:** Jede Cotton-Komponente erhält eine eigene Test-Ansicht (z.B. /test) mit Beispieldaten. Das erleichtert Entwicklung, Review und spätere Wartung.
- **Weitere Templates auf Cotton/DaisyUI umstellen** (z.B. Passwort-Reset)
- **Mehr DaisyUI-Komponenten als Cotton-Wrapper**
- **Tests und Dokumentation aktualisieren**
- **Clean-Up:** Nicht mehr genutzte Templates entfernen

---

## 3. Offene Fragen

- Zusätzliche Transaktionstypen oder Limits?
- Weitere Social-Login-Anbieter erwünscht?
- Erweiterte Statistiken und Exportfunktionen?

---

## 4. Gelöschte/veraltete Dateien

- kaffee/templates/kaffee/partials/einlage_form.html
- kaffee/templates/kaffee/partials/kontoauszug_liste.html
- kaffee/templates/kaffee/components/transaction_table.html
- kaffee/templates/kaffee/components/transaction_row.html

---
**Bitte diese Datei regelmäßig ergänzen und als Fahrplan für die Entwicklung nutzen!**
