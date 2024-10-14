#!/usr/bin/env python3
import argparse
from language import Language
from anki import Anki

def add_note(anki, language, word):
  if anki.check_note_exists(language.deck, word, language.query_fields):
    print(f"Note for {word} already exists")
  else:
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
    print(anki.add_note(note))


def main():
  # Possible script inputs
  LANGUAGE_OPTIONS = ("polish", "english")
  ADD_NOTE = "addNote"
  ADD_MODEL = "addModel"
  MODIFY_MODEL = "modifyModel"
  COMMAND_OPTIONS = (ADD_NOTE, ADD_MODEL, MODIFY_MODEL)

  argParser = argparse.ArgumentParser(
    prog="anky.py",
    description="It automatically creates Polish vocabulary flash cards in Anki"
  )
  argParser.add_argument("command", choices=COMMAND_OPTIONS)
  argParser.add_argument("language", choices=LANGUAGE_OPTIONS)
  argParser.add_argument("word", type=str)
  args = argParser.parse_args()

  print(f"Command: {args.command}")
  language = Language(args.language)
  word = args.word
  anki = Anki()

  match args.command:
    case ADD_NOTE:
      add_note(anki, language, word)


if __name__ == "__main__":
  main()
