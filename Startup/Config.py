from pathlib import Path
import os

# ----- Model Name ----- #

model_name = "llama3.2"

# ----- Personality Prompt -----#

personality_prompt = ""

def Get_Personality_Prompt():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(base_dir, 'Prompts', 'personality_prompt.txt')
    with open(prompt_path, "r") as f:
        personality_prompt = f.read()