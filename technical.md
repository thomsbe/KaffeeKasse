# Technische Dokumentation KaffeeKasse

## Technologie-Stack

### Backend
- Django – Hauptframework für die Webanwendung
- Django-Allauth – Für Nutzer-Registrierung, Login und Social Login (Google, GitHub, Microsoft)
- Django-Cotton – Für verbesserte Entwicklererfahrung

### Frontend
- Tailwind CSS – Utility-first CSS Framework
- DaisyUI – Komponenten-Bibliothek für Tailwind

## Technische Entscheidungen

### Django
- Gewählt wegen der robusten ORM
- Eingebautes Admin-Interface
- Große Community und viele verfügbare Packages

### Django-Allauth
- Ermöglicht Nutzer-Registrierung und Login
- Unterstützt Social Login (Google, GitHub, Microsoft)
- Flexible Anpassung der Authentifizierung

### Tailwind + DaisyUI
- Moderne UI-Entwicklung
- Schnelle Prototypen-Entwicklung
- Konsistentes Design-System
- DaisyUI bietet fertige Komponenten

### Django-Cotton
- Verbesserte Entwicklererfahrung
- Besseres Debugging
- Hilfreiche Entwickler-Tools

## Erkenntnisse: Tailwind CSS v4 & DaisyUI Integration

### Wichtige Hinweise für das Setup (Stand 2025)

#### 1. Quellenangabe für Tailwind-Klassen
- **Ab Tailwind v4 werden die zu scannenden Dateien nicht mehr in der tailwind.config.js angegeben, sondern direkt in der styles.css mit `@source`.**
- Beispiel:
  ```css
  @source "../../../**/*.{html,py,js}";
  ```

#### 2. DaisyUI-Integration
- **DaisyUI wird als Plugin eingebunden.**
- Empfohlen: Direkt in der styles.css mit
  ```css
  @plugin "daisyui";
  ```
- Alternativ/zusätzlich in der tailwind.config.js:
  ```js
  module.exports = {
    plugins: [require('daisyui')],
  }
  ```

#### 3. Minimalbeispiel für styles.css
```css
@import "tailwindcss";
@plugin "daisyui";
@source "../../../**/*.{html,py,js}";
```

#### 4. Nach Neuinstallation von django-tailwind
- **Alle zusätzlichen npm-Pakete (wie DaisyUI) müssen erneut installiert werden:**
  ```sh
  npm install daisyui@latest --save-dev
  ```
- Die eigene tailwind.config.js und base.html können durch das Init überschrieben werden und müssen ggf. wiederhergestellt werden.

#### 5. Build-Prozess
- Nach jeder Änderung oder Neuinstallation:
  ```sh
  python manage.py tailwind start
  ```
- Prüfen, ob DaisyUI-Klassen wie `.btn` im Build (styles.css) auftauchen.

---
**Diese Hinweise unbedingt beachten, um Frust bei zukünftigen Updates oder Neuinstallationen zu vermeiden!**

Stand: 23.04.2025
