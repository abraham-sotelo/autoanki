#!/usr/bin/env python3
import json

def form_noun_model(language, word):
  fieldNounName = [f"{y}-{x}" for y in language.quantities for x in language.cases]
  fieldsNoun = tuple({"name": f'{language.deck}-{field}'} for field in fieldNounName)
  print("Noun model:")
  model = {
    "model": word,
    "fields": fieldsNoun,
  }
  print(json.dumps(model, indent=4, ensure_ascii=False))
  return model


def form_note(deck, model, fields):
  return {
    "note": {
      "deckName": deck,
      "modelName": model,
      "fields": fields,
      "options": {
        "allowDuplicate": False,
        "duplicateScope": deck
      }
    }
  }
note = {
      "note": {
        "deckName": "My-deck",
        "modelName": "Basic",
        "fields": {
          "Front": "Perro",
          "Back": "Pies"
        },
        "options": {
          "allowDuplicate": False,
          "duplicateScope": "My-deck"
        }
      }
    }
