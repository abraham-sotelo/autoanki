#!/usr/bin/env python3
import argparse
import json
import src.anki as anki
import src.chatGPT as chatGPT
import src.notes as notes
from src.language import Language
from src.logger import logger

def add_note(language, word):
  language = Language(language)
  if anki.check_note_exists(language.deck, word, language.query_fields):
    print(f"Note for {word} already exists")
  else:
    prompt = language.get_prompt().replace("#word#", f'"{word}"')
    logger.debug("ChatGPT prompt: " + prompt)

    #response = chatGPT.send_prompt(prompt)
    response = {"type": "Rzeczownik", "Angielski": "doggy", "Polski-pojedyncza-mianownik": "pies", "Polski-pojedyncza-dopełniacz": "psa", "Polski-pojedyncza-celownik": "psu", "Polski-pojedyncza-biernik": "psa", "Polski-pojedyncza-narzędnik": "psem", "Polski-pojedyncza-miejscownik": "psie", "Polski-pojedyncza-wołacz": "psie", "Polski-mnoga-mianownik": "psy", "Polski-mnoga-dopełniacz": "psów", "Polski-mnoga-celownik": "psom", "Polski-mnoga-biernik": "psy", "Polski-mnoga-narzędnik": "psami", "Polski-mnoga-miejscownik": "psach", "Polski-mnoga-wołacz": "psy"}
    model = response.pop("type")
    note = notes.form_note("My-deck", model, response)
    anki.add_note(note)


def perform_action(action, argParams):
  if argParams.endswith(".json"):
    with open(argParams) as jsonFile:
      params = json.load(jsonFile)
  elif argParams.startswith("{"):
    params = json.loads(argParams)
  else:
    print("Not valid params detected, using an empty dictionary")
    params = {}
  response = anki.perform_action(action, params)
  print(json.dumps(response, indent=4, ensure_ascii=False))


def main():
  LANGUAGE_OPTIONS = ("polish", "english")
  ADD_NOTE = "addNote"
  ACTION = "action"

  # Top level argument parser
  argParser = argparse.ArgumentParser(
    prog="anky.py",
    description="It automatically creates Polish vocabulary flash cards in Anki"
  )
  subparsers = argParser.add_subparsers(dest="command", required=True)
  # Subparser for the addNote command
  addNoteParser = subparsers.add_parser(ADD_NOTE)
  addNoteParser.add_argument("language", choices=LANGUAGE_OPTIONS)
  addNoteParser.add_argument("word", type=str)
  # Subparser for the action command
  actionParser = subparsers.add_parser(ACTION)
  actionParser.add_argument("action", type=str)
  actionParser.add_argument("params", type=str)
  args = argParser.parse_args()

  if args.command == ADD_NOTE:
    add_note(args.language, args.word)
  elif args.command == ACTION:
    perform_action(args.action, args.params)
  else:
    print("Invalid command")


if __name__ == "__main__":
  main()
