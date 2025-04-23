# Kaffeekassen-App: Konzept & Plan

## Ziel
Eine Django-App zur Verwaltung einer Kaffeekasse mit Nutzerkonten, Einlagen und individuellem Kaffeekonsum. Die App soll fair, transparent und flexibel sein.

## Grundprinzipien
- Jeder Nutzer hat ein Konto (Guthaben).
- Nutzer können Kaffeebohnen (bzw. deren Wert) einbringen und konsumieren.
- Wer Bohnen einbringt, erhält ein Guthaben (z. B. 10 € für 1 kg Bohnen).
- Konsum wird als „Schulden“ gegenüber dem Pool bzw. den Einbringenden verbucht.
- Die Kosten werden fair auf alle Nutzer verteilt.

## Beispiel
- Nutzer A bringt 1 kg Bohnen für 10 €.
- 5 Nutzer konsumieren jeweils gleich viel.
- Jeder hat 2 € „Schulden“.
- Nutzer A hat 10 € eingebracht, 2 € konsumiert → 8 € Guthaben.

## Neue Nutzer
- Neue Nutzer starten mit 0 € Guthaben.
- Sie „kaufen sich ein“, indem sie Guthaben aufladen (Bohnen mitbringen oder Geld einzahlen).

## Erweiterung: Mahlvorgänge & Konsumprofile
- Jeder Kaffeevorgang kann unterschiedlich viele Mahlvorgänge haben (z. B. Espresso 2x, Filterkaffee 1x).
- Für jeden Nutzer kann ein individuelles Konsumprofil erstellt werden (wie oft, wie viel, wie gemahlen).
- Die Abrechnung erfolgt pro Mahlvorgang, um den Verbrauch fair zu berechnen.
- Statistiken und Auswertungen pro Nutzer sind möglich.

## Berechnung des Kaffeewerts
- Der Wert eines Kaffees ergibt sich aus:
  - Preis pro kg Bohnen (z. B. 9 €/kg)
  - Durchschnittlicher Verbrauch pro Tasse (z. B. 8 g)
- Diese Basiswerte werden in einer eigenen Tabelle/Modell gespeichert (z. B. „KaffeeKonfiguration“).
- Beispiel: 1 kg = 1000 g = 9 €, 1 Tasse = 8 g → 1 Tasse kostet 0,072 €

## Modell-Ideen (Django)
- `User`: Django-User-Modell (ggf. erweitert um Profilfelder)
- `KaffeeKonfiguration`: Preis/kg, Gramm/Tasse, Stand: Datum
- `Konsum`: Nutzer, Datum, Anzahl Tassen, Mahlvorgänge
- `Einlage`: Nutzer, Datum, Menge (kg/g), Wert (€)
- `Transaktion`: Abstraktes Modell für Einlagen und Konsum (optional)

## Vorteile
- Individuelle, faire Abrechnung nach realem Verbrauch
- Flexible Anpassung der Basiswerte
- Transparenz und Motivation zum Mitmachen
- Erweiterbar für Statistiken, Nutzerklassen, Rollen u. v. m.

## Offene Punkte
- Gramm pro Tasse muss noch ermittelt werden (z. B. durch Wiegen oder Recherche)
- Rollenverwaltung und Nutzerklassen sind als spätere Erweiterung möglich

---
Stand: 23.04.2025

