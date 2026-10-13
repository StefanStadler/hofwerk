# Hofwerk

Persönlicher Plugin-Marketplace für Claude: Werkzeuge für Hof, Steuer, PV und Betrieb.

## Plugins

| Plugin | Zweck |
|---|---|
| [`fiskus`](plugins/fiskus/README.md) | Steuer-Workflow: Belege sortieren, Online-Rechnungen laden, Steuerlast schätzen, Umsatzsteuer vorbereiten |

## Installation

```
/plugin marketplace add <pfad-oder-repo>
/plugin install fiskus@hofwerk
```

## Neues Plugin hinzufügen

1. Ordner `plugins/<name>/` mit `.claude-plugin/plugin.json` und `skills/` anlegen.
2. Eintrag in `.claude-plugin/marketplace.json` ergänzen (`"source": "./plugins/<name>"`).
