import unittest
import json
from unittest.mock import patch, call
import src.anki as anki

class TestAnki(unittest.TestCase):

  @patch("src.anki.requests.post")
  def test_perform_action(self, mock_post):
    test_cases = [
      {"msg": "Test with correct action and params",
       "action": "action", "params": {"param": "value"}, "expectedResult": {"result": "test"}},
      {"msg": "Test with wrong action",
       "action": "wrongAction", "params": {"param": "value"}, "expectedResult": {"result": None, "error": "Unsupported action"}},
      {"msg": "Test with wrong parameters",
       "action": "action", "params": {"wrongParam": "value"}, "expectedResult": {'result': None, "error": "Unexpected parameter"}},
      {"msg": "Test with wrong type in action",
       "action": 1, "params": {"param": "value"}, "expectedResult": {"error": "1 is not type string"}},
      {"msg": "Test with wrong type in params",
       "action": 1, "params": {"param": "value"}, "expectedResult": {"error": "1 is not type object"}},
    ]
    for case in test_cases:
      with self.subTest(msg = f"{case["msg"]}"):
        action = case["action"]
        params = case["params"]
        expectedResult = case["expectedResult"]
        mock_post.return_value.json.return_value = expectedResult
        result = anki.perform_action(action, params)
        self.assertEqual(result, expectedResult)

  @patch('builtins.print')
  @patch("src.anki.requests.post")
  def test_check_note_exists(self, mock_post, mock_print):
    test_cases = [
      {"msg": "Test with correct deck, note and fields",
       "deck": "deck", "note": "note", "fields": ["field1", "field2"], "expectedResult": True},
      {"msg": "Test with wrong deck",
       "deck": "wrongDeck", "note": "note", "fields": ["field1", "field2"], "expectedResult": False},
      {"msg": "Test with wrong note",
       "deck": "deck", "note": "wrongNote", "fields": ["field1", "field2"], "expectedResult": False},
      {"msg": "Test with wrong fields",
       "deck": "deck", "note": "note", "fields": ["wrongField1", "wrongField2"], "expectedResult": False},
    ]
    for case in test_cases:
      with self.subTest(msg = f"{case["msg"]}"):
        deck = case["deck"]
        note = case["note"]
        fields = case["fields"]
        expectedResult = case["expectedResult"]
        mock_post.return_value.json.return_value = {"result": ["note1", "note2"]} if expectedResult else {"result": []}
        result = anki.check_note_exists(deck, note, fields)
        self.assertEqual(result, expectedResult)
        mock_print.assert_called_with(f"deck:{deck} "+" OR ".join([f"{field}:{note}" for field in fields]))


  @patch('builtins.print')
  @patch("src.anki.requests.post")
  def test_add_note(self, mock_post, mock_print):
    test_cases = [
      {"msg": "Adding note",
       "note": "note", "expectedResult": True},
      {"msg": "Trying to add duplicated note",
       "note": "duplicatedNote", "expectedResult": False},
      {"msg": "Trying to add bad note",
       "note": "badNote", "expectedResult": False},
    ]
    for case in test_cases:
      with self.subTest(msg = f"{case["msg"]}"):
        note = case["note"]
        expectedResult = case["expectedResult"]
        if expectedResult:
          response = {"result": 11111, "error": None}
        else:
          response = {"result": None, "error": "Error"}
        mock_post.return_value.json.return_value = response
        result = anki.add_note(note)
        self.assertEqual(result, expectedResult)
        mock_print.assert_has_calls([
          call(f"Adding note:\n{json.dumps(note, indent=4)}"),
          call(f"Response: {json.dumps(response, indent=4)}")
        ], any_order=False)


if __name__ == '__main__':
    unittest.main()