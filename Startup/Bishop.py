import ollama
import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from Config import (
    model_name,
    personality_prompt,
    Get_Personality_Prompt,
)

personality_prompt = Get_Personality_Prompt()
print(personality_prompt)

# Variables
response = ""
who = 1
user_input = ""
messages = [
    {'role': 'system', 'content': personality_prompt},
    {'role': 'user', 'content': "Hello!"},
]


while True:
    user_input = input("Message: ")
    if (user_input == "exit"
        ): break
    messages = [
        {'role': 'system', 'content': personality_prompt},
        {'role': 'user', 'content': user_input}
    ]
    who = 1
    from Modules.Memory import Save_Message
    Save_Message(response, who, user_input)
    response = ollama.chat(model=model_name, messages=messages)
    who = 0
    Save_Message(response, who, user_input)
    answer = response.message.content
    print(answer)