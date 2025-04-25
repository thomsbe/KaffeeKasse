# Technische Dokumentation KaffeeKasse

## Stand: 25.04.2025

---

## 1. Technologie-Stack

### Backend
- Django 5.2
- Django-Allauth (Account-Management & Social Login)
- django-htmx (dynamische Partial-Updates)
- django-browser-reload (Auto-Reload im Dev-Modus)
- Whitenoise (statische Dateien)
- SQLite (Entwicklung), später PostgreSQL oder MySQL
- uv (Python-Dependency-Management & Installation)

### Frontend
- Tailwind CSS v4
- DaisyUI 5 als Plugin
- HTMX 1.9.10 für Modals & Infinite-Loading
- Alpine.js für Modals und dynamische UI-Elemente (Einbindung via CDN in base.html erforderlich)
- **Django-Cotton** für UI-Komponenten

**Hinweis:** Für alle Cotton-Komponenten gelten die verbindlichen Regeln und Best Practices aus der Datei [.cursor/rules/django-cotton.mdc]. Diese Datei ist für alle LLMs und Entwickler maßgeblich und muss bei jeder Komponentenerstellung und -änderung berücksichtigt werden.

---

## 2. Architektur & Datenmodell

- Zentrales Modell `Transaktion` mit Feldern: `typ`, `nutzer`, `datum`, `saldo_wert`, `beschreibung`.
- Subklassen (`KaffeeEinlage`, `GeldEinzahlung`, `Wochenverbrauch`, `Auszahlung`) per Django Multi-Table Inheritance.
- Views:
  - `index`: rendert Startseite, liefert Kontext für Auth-Status, Kontostand und Transaktionsliste.
  - `einlage`: HTMX-GET/POST für Formular-Partial und Success-Partial.
- Templates:
  - `kaffee/index.html`: personalisierte Hero- bzw. Transaktionsansicht.
  - Partials in `kaffee/partials/`: `einlage_success.html`, `kontoauszug_liste.html`.
- URL-Konfiguration:
  - Custom Redirect `/accounts/profile/` → `/`
  - Allauth-Routes in `main/urls.py`
  - App-Routes in `kaffee/urls.py`

---

## 3. Build & Deployment

1. **Abhängigkeiten installieren**
   ```pwsh
   uv pip install -r requirements.txt
   uv pip install django-htmx django-browser-reload
   ```
2. **Tailwind-Entwicklung**
   - In `theme/static_src/src/styles.css`:
     ```css
     @import "tailwindcss";
     @plugin "daisyui";
     @source "../../../**/*.{html,py,js}";
     ```
   - Dev-Server starten:
     ```pwsh
     python manage.py tailwind start
     ```
3. **Django-Server starten**
   ```pwsh
   python manage.py runserver
   ```
4. **Für Produktion**
   - `DEBUG=False`, Umgebungsvariablen setzen (`SECRET_KEY`, `ALLOWED_HOSTS`).
   - `python manage.py collectstatic`
   - Datenbank-Migrationen: `python manage.py migrate`

---

## Komponenten-Architektur & UI

- Cotton-Komponenten für alle zentralen UI-Elemente (Buttons, Modals, Formulare, Listen, Badges, Pagination, Hero)
- DaisyUI v5 als CSS-Framework, keine eigene CSS nötig
- HTMX für dynamische Formulare/Interaktionen
- Alpine.js für Modals (Einbindung via CDN in base.html!)

## Refactoring-Details

- Account-Templates (login, signup) auf Cotton/DaisyUI refaktorisiert
- Fehlerbehebung: c-button prüft jetzt auf content/label, Modal korrekt steuerbar
- Neue Komponente: cotton/hero.html
- Alte, nicht mehr genutzte Partials/Komponenten entfernt (siehe unten)

## Hinweise für Entwickler

- Cotton-Komponenten werden als <c-xyz> verwendet, Block-Content via {{ content|safe }}
- Buttons: <c-button>Text</c-button> oder <c-button label="Text" />
- Modals: <c-modal open=true>...</c-modal>, Alpine.js muss geladen sein
- DaisyUI-Klassen via extra_classes-Attribut
- Neue Komponenten: Datei in templates/cotton/ anlegen, Naming beachten
- Python-Dependencies mit 'uv pip install ...' (siehe Projekt-Memory)

## Gelöschte/veraltete Dateien

- kaffee/templates/kaffee/partials/einlage_form.html
- kaffee/templates/kaffee/partials/kontoauszug_liste.html
- kaffee/templates/kaffee/components/transaction_table.html
- kaffee/templates/kaffee/components/transaction_row.html

---

## Komponenten-Teststrategie

- **Alle Cotton-Komponenten** (z.B. Tabellen, Zeilen, Formulare) erhalten eine eigene Test-Ansicht (z.B. /test), in der sie mit Beispieldaten isoliert gerendert werden.
- Für die Erstellung und Pflege dieser Komponenten gelten die verbindlichen Cotton-Regeln aus [.cursor/rules/django-cotton.mdc].
- Änderungen an Komponenten müssen immer im Einklang mit diesen Vorgaben erfolgen.

---

**Diese Datei bitte aktuell halten, damit Setup, Architektur und Arbeitsweise stets klar sind!**
