# Projektplan: KaffeeKasse

## Stand: 23.04.2025

---

## 1. Was wurde bisher umgesetzt?

- **Projektidee und technische Rahmenbedingungen** sind dokumentiert in [idee.md] und [technical.md].
- **Django-Projekt aufgesetzt** mit folgenden Features:
  - User-Management mit Django-Allauth
  - Tailwind CSS v4 Integration für modernes CSS
  - DaisyUI als UI-Komponenten-Bibliothek
  - Responsive Layout und Navigation mit DaisyUI
  - Konsum-, Einlage- und Nutzerprofil-Modelle inkl. Admin-Interface
  - Automatischer Browser-Reload im Dev-Modus
- **Wichtige Stolperfallen dokumentiert** (z.B. Tailwind v4: Quellenangabe via @source in CSS, DaisyUI-Integration, Verhalten nach Neuinstallation)
- **Allauth-Templates für Login und Registrierung** wurden kopiert und mit DaisyUI-Komponenten gestaltet (weitere Anpassungen möglich)
- **Zentrales Auth-Layout (entrance.html)** im DaisyUI-Stil angelegt (funktioniert ggf. noch nicht wie gewünscht, siehe ToDos)

---

## 2. Was muss noch getan werden? (ToDos)

- **Allauth-Templates weiter anpassen:**
  - Prüfen, warum das DaisyUI-Layout bei allen Auth-Seiten noch nicht überall greift
  - Weitere Templates (Passwort-Reset, E-Mail-Bestätigung etc.) anpassen
- **Testing & Validierung:**
  - Unit- und Integrationstests für alle Kernfunktionen
  - Testfälle für Authentifizierung und Konsum-Logik
- **Fehlerbehandlung & Logging:**
  - Logging für wichtige Aktionen und Fehler
  - Fehlermeldungen für Nutzer verbessern
- **Design & Usability:**
  - UI-Feinschliff: Buttons, Farben, Responsiveness
  - Barrierefreiheit prüfen
- **Dokumentation:**
  - README aktualisieren (Beispiele, Nutzung, Entwicklerhinweise)
  - Changelog pflegen
- **Deployment-Vorbereitung:**
  - Einstellungen für Produktion (SECRET_KEY, Debug, Allowed Hosts)
  - Collectstatic, Datenbankmigrationen
  - Evtl. Dockerfile oder Deployment-Skripte

---

## 3. Offene Fragen / Wünsche

- Sollen weitere Features (z.B. Statistiken, Push-Benachrichtigungen) integriert werden?
- Gibt es Wünsche für spezielle Rollen/Rechte oder Integrationen (z.B. Slack, E-Mail)?
- Welche Auth-Provider (Google, GitHub etc.) sollen evtl. ergänzt werden?

---

**Bitte diese Datei regelmäßig ergänzen und als Fahrplan für die Entwicklung nutzen!**

