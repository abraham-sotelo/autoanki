#!/usr/bin/env python3
import argparse
from language import Language
import anki
import chatGPT
import notes
import json

def add_note(language, word):
  if anki.check_note_exists(language.deck, word, language.query_fields):
    print(f"Note for {word} already exists")
  else:
    prompt = language.get_prompt().replace("#word#", f'"{word}"')
    print("ChatGPT prompt: " + prompt)

    #response = chatGPT.send_prompt(prompt)
    response = {"type": "Rzeczownik", "Angielski": "doggy", "Polski-pojedyncza-mianownik": "pies", "Polski-pojedyncza-dopełniacz": "psa", "Polski-pojedyncza-celownik": "psu", "Polski-pojedyncza-biernik": "psa", "Polski-pojedyncza-narzędnik": "psem", "Polski-pojedyncza-miejscownik": "psie", "Polski-pojedyncza-wołacz": "psie", "Polski-mnoga-mianownik": "psy", "Polski-mnoga-dopełniacz": "psów", "Polski-mnoga-celownik": "psom", "Polski-mnoga-biernik": "psy", "Polski-mnoga-narzędnik": "psami", "Polski-mnoga-miejscownik": "psach", "Polski-mnoga-wołacz": "psy"}
    model = response.pop("type")
    note = notes.form_note("My-deck", model, response)

    # Add the note to Anki
    print(anki.add_note(note))


def modify_model(language, word):
  if language.language == "polish":
    if word == "Rzeczownik":
      model = notes.form_noun_model(language, word)
      anki.update_model(model)
  return

  print("Modifying")
  notes.form_noun_model_fields(language)


def main():
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

  if args.command == ADD_NOTE:
    add_note(language, word)
  elif args.command == ADD_MODEL:
    pass
  elif args.command == MODIFY_MODEL:
    modify_model(language, word)
  else:
    print("Invalid command")


if __name__ == "__main__":
  main()
