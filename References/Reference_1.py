

# Basically this code just generates one response
# The stream = True part makes it print whilst generating
# See 'Using Ollama with Python: A Simple Guide' from Medium
from ollama import generate

for chunk in generate('llama3.2', 'Why is the sky blue?', stream = True):
    print(chunk['response'], end = '', flush = True)


