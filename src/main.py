#!/usr/bin/env python3
import argparse
from language import Language
from anki import Anki
import math

def main():
  # Possible script inputs
  language_options = ("polish", "english")

  argParser = argparse.ArgumentParser(
    prog="anky.py",
    description="It automatically creates Polish vocabulary flash cards in Anki"
  )
  argParser.add_argument("command", choices=("addNote", "addModel", "modifyModel"))
  argParser.add_argument("language", choices=language_options)
  argParser.add_argument("word", type=str)
  args = argParser.parse_args()

  print(args.command)
  language = Language(args.language)
  word = args.word
  anki = Anki()
  res = anki.check_note_exists(language.deck, word, language.query_fields)
  print(res)

if __name__ == "__main__":
  main()



