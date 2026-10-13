# Hofwerk

Persönlicher Plugin-Marketplace für Claude: Werkzeuge für Hof, Steuer, PV und Betrieb.

## Plugins

| Plugin | Zweck |
|---|---|
| [`fiskus`](plugins/fiskus/README.md) | Steuer-Workflow: Belege sortieren, Online-Rechnungen laden, Steuerlast schätzen, Umsatzsteuer vorbereiten |
| [`freiheit`](plugins/freiheit/README.md) | Finanzielle Freiheit: Fixkosten und Lebensbedarf berechnen, Deckungsgrad des passiven Einkommens prüfen |
| [`postfach`](plugins/postfach/README.md) | Gmail-Posteingang nach eigenen Regeln sortieren: Labels, Archiv, Papierkorb nach Freigabe |

## Installation

```
/plugin marketplace add <pfad-oder-repo>
/plugin install fiskus@hofwerk
/plugin install freiheit@hofwerk
/plugin install postfach@hofwerk
```

## Neues Plugin hinzufügen

1. Ordner `plugins/<name>/` mit `.claude-plugin/plugin.json` und `skills/` anlegen.
2. Eintrag in `.claude-plugin/marketplace.json` ergänzen (`"source": "./plugins/<name>"`).
