#!/usr/bin/env python3
import requests
import json

ANKI_URL = "http://localhost:8765"
VERSION = 6

class Anki:
  def __init__(self):
    pass

  def perform_action(self, action, params):
    payload = {
      "action": action,
      "version": VERSION,
      "params": params
    }
    res = requests.post(ANKI_URL, json=payload)
    return res.json()

  def check_note_exists(self, deck, note, fields):
    query_fields = [f"{field}:{note}" for field in fields]
    query = f"deck:{deck} "+" OR ".join(query_fields)
    print(query)
    response = self.perform_action("findNotes", {"query": query})
    return len(response["result"]) > 0

  def get_note_info(self, note_id):
    response = self.perform_action("notesInfo", {"notes": [note_id]})
    return json.dumps(response, indent=4)

  def add_note(self, note):
    print(f"Adding note:\n{json.dumps(note, indent=4)}")
    response = self.perform_action("addNote", note)
    print(f"Response: {json.dumps(response, indent=4)}")
    return type(response["result"]) == int
