from openai import OpenAI
import json
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("CHATGPT_API_KEY"),
)

def send_prompt(prompt):
  # OpenAI API call for version 1.0.0
  chat_completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "user", "content": prompt}],
  )
  print("\n\n============================\n\n")
  print(chat_completion.model_dump())
  print("\n\n============================\n\n")    
  print(chat_completion.model_dump_json(indent=4))
  print("\n\n============================\n\n")
  print(chat_completion.choices[0].message.content)
  return json.loads(chat_completion.choices[0].message.content)

# Example usage