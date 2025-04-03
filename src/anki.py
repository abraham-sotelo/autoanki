#!/usr/bin/env python3
import requests
import json
from src.logger import logger

def perform_action(action, params):
  payload = {
    "action": action,
    "version": 6,
    "params": params
  }
  res = requests.post("http://localhost:8765", json=payload)
  return res.json()

def check_note_exists(deck, note, fields):
  query_fields = [f"{field}:{note}" for field in fields]
  query = f"deck:{deck} "+" OR ".join(query_fields)
  logger.info("Check note exists - " + query)
  response = perform_action("findNotes", {"query": query})
  return len(response["result"]) > 0

def get_note_info(note_id):
  response = perform_action("notesInfo", {"notes": [note_id]})
  return json.dumps(response, indent=4)

def add_note(note):
  print(f"Adding note")
  logger.debug("Adding note - " + json.dumps(note, indent=4, ensure_ascii=False))
  response = perform_action("addNote", note)
  print(f"Error: {response['error']}" if response["error"] else f"Note added with ID: {response['result']}")
  logger.debug(f"Response: {json.dumps(response, indent=4)}")
  return type(response["result"]) == int

def update_model(model):
  print(f"Updating model")
  response = perform_action("updateModelTemplates", model)
  print(f"Response: {json.dumps(response, indent=4)}")
  return response["result"] == "Updated model"