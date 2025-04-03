# Anki Automation

This project allows to:
- Add notes
- Add models
- Modify models

It is possible to prompt ChatGPT to generate lists of the items that need to be added, create the models and notes in a format that Anki understands and write them into the Anki database using the Anki-Connect API

## Add notes
1. Ask ChatGPT for a python dictionary contaning: 
    * word
    * type of word (noun, verb,adjective)
    * variations (declensions or conjugations)
    * pattern (gender, conjugation group, etc)

2. Generate json object with the note information
3. Send post request to the Anki-Connect API

## Examples using the `action` command

Change field name:
```bash
 ./autoanki.py action modelFieldRename '{ "modelName": "Rzeczownik", "oldFieldName": "Angielski", "newFieldName": "Angielski-pojedyncza" }'

{
    "result": null,
    "error": null
}
 ```

Add new field:
```bash
./autoanki.py action modelFieldAdd '{ "modelName": "Rzeczownik", "fieldName": "Angielski-mnoga", "index": 8 }'

{
    "result": null,
    "error": null
}
```

Reposition field:
```bash
./autoanki.py action modelFieldReposition '{ "modelName": "Rzeczownik", "fieldName": "Angielski-mnoga", "index": 1 }'

{
    "result": null,
    "error": null
}
```

Check fields in a model
```bash
./autoanki.py action modelFieldNames '{ "modelName": "Rzeczownik" }'
{
    "result": [
        "Angielski-pojedyncza",
        "Angielski-mnoga",
        "Polski-pojedyncza-mianownik",
        "Polski-pojedyncza-dopełniacz",
        "Polski-pojedyncza-celownik",
        "Polski-pojedyncza-biernik",
        "Polski-pojedyncza-narzędnik",
        "Polski-pojedyncza-miejscownik",
        "Polski-pojedyncza-wołacz",
        "Polski-mnoga-mianownik",v
        "Polski-mnoga-dopełniacz",
        "Polski-mnoga-celownik",
        "Polski-mnoga-biernik",
        "Polski-mnoga-narzędnik",
        "Polski-mnoga-miejscownik",
        "Polski-mnoga-wołacz"
    ],
    "error": null
}
```

Check templates in model:
```bash
./autoanki.py action modelTemplates '{ "modelName": "Rzeczownik" }'

{
    "result": {
        "ENG-POL mianownik": {
            "Front": "{{Angielski-pojedyncza}} [mianownik]\n\n{{type:Polski-pojedyncza-mianownik}}",
            "Back": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Polski-pojedyncza-mianownik}}"
        },
        "POL-ENG mianownik": {
            "Front": "{{Polski-pojedyncza-mianownik}}",
            "Back": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Angielski-pojedyncza}}\n<br>\n<br>\n[nominative]"
        }
        ...
    }
        "error": null
}
```

Add card template
```bash
./autoanki.py action modelTemplateAdd ../json_params/ENG-POL-pojedyncza.json

{
    "result": null,
    "error": null
}
```
## Print additional debug info

To enable detailed debugging information, set the `DEBUG` environment variable to `1`,  when running the script. This will print additional logs to help with troubleshooting.

### Example

Run the script with debugging enabled:
```bash
DEBUG=1 ./autoanki.py addNote Polish dog
```

This will output detailed information about the script's execution, including API requests and responses.



## Ad-hoc manual modifications example
There are modifications that are going to be performed once that can rely on some python logic for parameters manipulation. In such cases, it makes sense to implement them manually in the python console.

### Rename and add fields
I needed to modify the noun fields in order to have singular and plural translations in the same note. So my approach was to rename the current fields to indicate that they are singular and add new plural fields.
```python
>>> import templates, language, notes, anki
>>> NUMBER_OF_FIELDS = 7
>>> language = language.Language("polish")
>>>
>>> # Rename singular fields
>>> # Get new field names from language template
>>> noun_model = notes.form_noun_model(language, "Rzeczownik")
>>> fields = noun_model["fields"]
>>> new_fields = []
>>> for field in fields:
...   for value in field.values():
...     new_fields.append(value)
>>> # Singular fields
>>> fields_sin = new_fields[:NUMBER_OF_FIELDS]
>>> # Get current field names from Anki
>>> res = anki.perform_action("modelFieldNames", {"modelName": "Rzeczownik"})
>>> old_fields = res["result"]
>>> # Rename fields
>>> i = 0
>>> for field in old_fields[1:]: # 1 -> ignores English field
...   anki.perform_action("modelFieldRename", { "modelName": "Rzeczownik", "oldFieldName": field, "newFieldName": new_fields[i] })
...   i += 1
...
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
>>>
>>> # Add plural fields
>>> for field in new_fields[NUMBER_OF_FIELDS:]:
...   anki.perform_action("modelFieldAdd", { "modelName": "Rzeczownik", "fieldName": field })
...
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
{'result': None, 'error': None}
>>>
>>> # Verify fields
>>> import json
>>> print(json.dumps(anki.perform_action("modelFieldNames", {"modelName": "Rzeczownik"}), indent=4, ensure_ascii=False))
{
    "result": [
        "Angielski",
        "Polski-pojedyncza-mianownik",
        "Polski-pojedyncza-dopełniacz",
        "Polski-pojedyncza-celownik",
        "Polski-pojedyncza-biernik",
        "Polski-pojedyncza-narzędnik",
        "Polski-pojedyncza-miejscownik",
        "Polski-pojedyncza-wołacz",
        "Polski-mnoga-mianownik",
        "Polski-mnoga-dopełniacz",
        "Polski-mnoga-celownik",
        "Polski-mnoga-biernik",
        "Polski-mnoga-narzędnik",
        "Polski-mnoga-miejscownik",
        "Polski-mnoga-wołacz"
    ],
    "error": null
}
>>>
```


## To Do
1. Create the plural fields in the nouns models (Probably I need to redisign the whole model)
2. Create the adjectives model
3. Extract the response from chatGPT (word, translation, grammar cases)
4. Create the template for the note
6. Add info about OpenAI api-key
7. Add Vscode debug
8. Project setup script: create venv, set vscode python intepreter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)