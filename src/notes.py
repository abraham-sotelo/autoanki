#!/usr/bin/env python3
import json

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

# Auxiliary functions
def form_noun_model(language, modelType):
  ''' Form a noun model for the given language.

  Args:
    language (str): The language for which the model is created.
    modelType (str): The model name, refers to the translation of the word "noun".

  Returns:
    dict: The model for the given language.

  Example:
    >>> form_noun_model("Language("polish"), "Rzeczownik")
    {
      "model": "Basic",
      "fields": [
        {'name': 'Polski-pojedyncza-mianownik'}
        {'name': 'Polski-pojedyncza-dopełniacz'}
        {'name': 'Polski-pojedyncza-celownik'}
        {'name': 'Polski-pojedyncza-biernik'}
        {'name': 'Polski-pojedyncza-narzędnik'}
        {'name': 'Polski-pojedyncza-miejscownik'}
        {'name': 'Polski-pojedyncza-wołacz'}
        {'name': 'Polski-mnoga-mianownik'}
        {'name': 'Polski-mnoga-dopełniacz'}
        {'name': 'Polski-mnoga-celownik'}
        {'name': 'Polski-mnoga-biernik'}
        {'name': 'Polski-mnoga-narzędnik'}
        {'name': 'Polski-mnoga-miejscownik'}
        {'name': 'Polski-mnoga-wołacz'}
      ]
    }
      '''
  fieldNounName = [f"{y}-{x}" for y in language.quantities for x in language.cases]
  fieldsNoun = tuple({"name": f'{language.deck}-{field}'} for field in fieldNounName)
  print("Noun model:")
  model = {
    "model": modelType,
    "fields": fieldsNoun,
  }
  print(json.dumps(model, indent=4, ensure_ascii=False))
  return model