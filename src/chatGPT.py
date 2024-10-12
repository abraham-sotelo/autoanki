from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("CHATGPT_API_KEY"),
)

def get_polish_word_info(word):
    prompt = f"""What is the grammatical type of the word {word}
              Provide ALL the conjugations, declensions, or cases based on the
              word type.
              Express your answer without any explanation as a RFC8259 compliant
              JSON where one of the keys is the type of word, and the rest of the 
              keys are the grammar case name, if a grammar case has multiple 
              variants use the following pattern:
              [singular-plural]-[masculine-feminine-neutral]-[gramar case].
              The keys must be in Polish, e.g. mnoga-męski-biernik
              The values most be the word tranlation to Polish"""
    
    prompt1 = "Give a Python tuple with the names of the Polish grammar genres in Polish"

    # OpenAI API call for version 1.0.0
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt1}],
    )
    print("\n\n============================\n\n")
    print(chat_completion.model_dump())
    print("\n\n============================\n\n")    
    print(chat_completion.model_dump_json(indent=4))
    print("\n\n============================\n\n")
    print(chat_completion.choices[0].message.content)

# Example usage
get_polish_word_info("tasty")