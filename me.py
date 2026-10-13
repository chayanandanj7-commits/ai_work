import requests
import os
import json

base_path=os.getcwd()

def create_folder(folder_name):
    actual_path=os.path.join(base_path,folder_name)
    os.makedirs(actual_path)





tools=[
    {
        "type":"function",
        "function":{
            "name":"create_folder",
            "description":"use to create folders",
            "parameters":{
                "type":"object",
                "properties":{
                    "folder_name":{
                        "type":"string",
                        "description":"name of the folder"
                    }
                },
                "required":["folder_name"]
            }

        }

    }
]






while True:
    user_input=input("you : ")
    if user_input =="exit":
        exit()
    else:


        message=[{
            "role":"user",
            "content":user_input

        }]

        response=requests.post(
            "http://localhost:11434/api/chat",
            json={
            "model":"qwen3:1.7b",
            "stream":False,
            "messages":message,
            "tools":tools
        }
        )
        data = response.json()
        

        print("\nAI response:")
        print(json.dumps(data["message"], indent=2))

    assistant_message = data["message"]

    tool_calls = assistant_message.get("tool_calls", [])

    for tool_call in tool_calls:

        function_name = tool_call["function"]["name"]

        arguments = tool_call["function"]["arguments"]

        if function_name == "create_folder":

            folder_name = arguments["folder_name"]

            create_folder(folder_name)

            print("\nFolder created:", folder_name)
            






