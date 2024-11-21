languages = {
  "polish": {
    "deck": "Polski",
    "query_fields": ("Angielski", "Hiszpański"),
    "types": ("Rzeczownik", "Czasownik", "Przymiotnik", "Przysłówek", "Zaimek", "Przyimek", "Spójnik", "Wykrzyknik", "Pytajnik"),
    "cases": ("mianownik", "dopełniacz", "celownik", "biernik", "narzędnik", "miejscownik", "wołacz"),
    "genders": ("męski", "żeński", "nijaki"),
    "quantities": ("pojedyncza", "mnoga"),
    "prompt": (
      'What is the grammatical type of the word #word#? '
      'Provide all the gramatical cases, declensions or conjugations based on the word type. '
      'Provide your answer without any explanation as an python dictionary. '
      'The first item must be the type of word, '
      'The next item the word in English. '
      'And the rest of the items the grammar cases in Polish. '
      'Do not add the "```python" language indicator to your response. '
      'For example, if the word is "dog", your answer should look like this:\n'
      '{'
      '"type": "Rzeczownik", '
      '"Angielski": "dog", '
      '"Polski-pojedyncza-mianownik": "pies", '
      '"Polski-pojedyncza-dopełniacz": "psa", '
      '"Polski-pojedyncza-celownik": "psu", '
      '"Polski-pojedyncza-biernik": "psa", '
      '"Polski-pojedyncza-narzędnik": "psem", '
      '"Polski-pojedyncza-miejscownik": "psie", '
      '"Polski-pojedyncza-wołacz": "psie", '
      '"Polski-mnoga-mianownik": "psy", '
      '"Polski-mnoga-dopełniacz": "psów", '
      '"Polski-mnoga-celownik": "psom", '
      '"Polski-mnoga-biernik": "psy", '
      '"Polski-mnoga-narzędnik": "psami", '
      '"Polski-mnoga-miejscownik": "psach", '
      '"Polski-mnoga-wołacz": "psy"'
      '}'
    )
  }
}
