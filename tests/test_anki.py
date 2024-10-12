import unittest
from unittest.mock import patch, MagicMock
from src.anki import Anki

class TestAnki(unittest.TestCase):

  @patch('src.anki.requests.post')
  def test_perform_action(self, mock_post):
    expectedResult = {"result": "test"}
    mock_post.return_value.json.return_value = expectedResult
    
    anki = Anki()
    action = "action"
    params = {"param": "value"}
    result = anki.perform_action(action, params)

    self.assertEqual(result, expectedResult)
      
if __name__ == '__main__':
    unittest.main()