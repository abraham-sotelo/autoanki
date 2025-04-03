languages = {
  "polish": {
    "deck": "Polski",
    "query_fields": ("Angielski", "Hiszpański"),
    "cases": ("mianownik", "dopełniacz", "celownik", "biernik", "narzędnik", "miejscownik", "wołacz"),
    "genders": ("męski", "żeński", "nijaki"),
    "quantities": ("pojedyncza", "mnoga"),
    "models": {
      "noun": {
        "name": "Rzeczownik",
        "types": ("cases", "quantities")
      },
      "adjective": {
        "name": "Przymiotnik",
        "types": ("cases", "genders", "quantities")
      },
    },
    "prompt": (
      'What is the grammatical type of the word #word#? '
      'Provide all the gramatical cases, declensions or conjugations in Polish based on the word type. '
      'Provide your answer without any explanation as a python dictionary. '
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
      'If the word is new, your answer should look like this:\n'
      '{'
      '"type": "Przymiotnik", '
      '"Angielski": "new", '
      '"Polski-pojedyncza-mianownik-męski": "nowy", '
      '"Polski-pojedyncza-mianownik-żeński": "nowa", '
      '"Polski-pojedyncza-dopełniacz-męski": "nowego", '
      '"Polski-pojedyncza-dopełniacz-żeński": "nowej", '
      '"Polski-pojedyncza-celownik-męski": "nowemu", '
      '"Polski-pojedyncza-celownik-żeński": "nowej", '
      '"Polski-pojedyncza-biernik-męski": "nowego", '
      '"Polski-pojedyncza-biernik-żeński": "nową", '
      '"Polski-pojedyncza-narzędnik-męski": "nowym", '
      '"Polski-pojedyncza-narzędnik-żeński": "nową", '
      '"Polski-pojedyncza-miejscownik-męski": "nowym", '
      '"Polski-pojedyncza-miejscownik-żeński": "nowej", '
      '"Polski-pojedyncza-wołacz-męski": "nowy", '
      '"Polski-pojedyncza-wołacz-żeński": "nowa", '
      '"Polski-mnoga-mianownik-męski": "nowi", '
      '"Polski-mnoga-mianownik-żeński": "nowe", '
      '"Polski-mnoga-dopełniacz-męski": "nowych", '
      '"Polski-mnoga-dopełniacz-żeński": "nowych", '
      '"Polski-mnoga-celownik-męski": "nowym", '
      '"Polski-mnoga-celownik-żeński": "nowym", '
      '"Polski-mnoga-biernik-męski": "nowych", '
      '"Polski-mnoga-biernik-żeński": "nowe", '
      '"Polski-mnoga-narzędnik-męski": "nowymi", '
      '"Polski-mnoga-narzędnik-żeński": "nowymi", '
      '"Polski-mnoga-miejscownik-męski": "nowych", '
      '"Polski-mnoga-miejscownik-żeński": "nowych", '
      '"Polski-mnoga-wołacz-męski": "nowi", '
      '"Polski-mnoga-wołacz-żeński": "nowe"'
      '}'
    )
  }
}