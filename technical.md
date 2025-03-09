# Technische Dokumentation

## Framework
- Django als Web Framework
- Python als Programmiersprache

## Projekt Setup
- Projektname: main
- App Name: kaffee
- Sprache: Deutsch (de-de)
- Zeitzone: Europe/Berlin

## Dependencies
- Django >= 5.1.7
- Python >= 3.12

## Entwicklungsumgebung
- Lokaler Development Server
- SQLite als Entwicklungsdatenbank
- UV als Package Manager

## Code-Qualität
- Ruff >= 0.9.10 als Linter
- Maximale Zeilenlänge: 100 Zeichen
- Aktivierte Regel-Sets:
  - E (pycodestyle)
  - F (pyflakes)
  - B (flake8-bugbear)
  - I (isort)
  - N (pep8-naming)
  - UP (pyupgrade)
  - DJ (flake8-django)
- Import-Sortierung nach Kategorien:
  1. Future
  2. Standard Library
  3. Django
  4. Third Party
  5. First Party
  6. Local Folder
