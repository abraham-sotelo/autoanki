import unittest
from unittest.mock import patch, MagicMock
from src.anki import Anki

class TestAnki(unittest.TestCase):

  @patch('src.anki.requests.post')
  def test_perform_action(self, mock_post):
    anki = Anki()
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


if __name__ == '__main__':
    unittest.main()