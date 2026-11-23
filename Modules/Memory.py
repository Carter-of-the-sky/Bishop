import json
import datetime
import os

time_date = ""
message = ""
role = ""
dir = ""
save = {
    "time_date": '',
    "message": '',
    "role": '',
    }

def Save_Message(response, who, user_input):
    dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(dir, "Memory", "current_conversation.json")
    if (who == 0):
        time_date = response.created_at
        message = response.message.content
        role = response.message.role
        save["time_date"] = time_date
        save["message"] = message
        save["role"] = role
        print(os.getcwd())
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(save, file, indent=4)
        print(save)
    else:
        time_date = datetime.datetime.now().isoformat()
        message = user_input
        role = 'user'
        save["time_date"] = time_date
        save["message"] = message
        save["role"] = role
        print(os.getcwd())
        with open("current_conversation.json", "w", encoding="utf-8") as file:
            json.dump(save, file, indent=4)
        print(save)