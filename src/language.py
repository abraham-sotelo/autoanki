from src.templates import languages

class Language:
  def __init__(self, language):
    self.language = language
    self.deck = languages[language]["deck"]
    self.query_fields = languages[language]["query_fields"]
    self.cases = languages[language]["cases"]
    self.genres = languages[language]["genders"]
    self.quantities = languages[language]["quantities"]
    self.models = languages[language]["models"]
    self.prompt = languages[language]["prompt"]
    
  def get_language(self):
    return self.language
  
  def get_cases(self):
    return self.cases
  
  def get_genres(self):
    return self.genres
  
  def get_quantities(self):
    return self.quantities

  def get_prompt(self):
    return self.prompt
