import requests
import os
import json


BASE_PATH = "D:\\chayanandan\\ai_computer_agent"


def create_folder(folder_name):
    path = os.path.join(BASE_PATH, folder_name)

    try:
        os.makedirs(path, exist_ok=True)
        return f"Folder created successfully: {path}"
    except Exception as e:
        return f"Error: {e}"


tools = [
    {
        "type": "function",
        "function": {
            "name": "create_folder",
            "description": "Create a new folder inside the AI agent project directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder_name": {
                        "type": "string",
                        "description": "The name of the folder to create"
                    }
                },
                "required": ["folder_name"]
            }
        }
    },

      {
        "type": "function",
        "function": {
            "name": "delete_folder",
            "description": "delete a  folder inside the AI agent project directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder_name": {
                        "type": "string",
                        "description": "The name of the folder to delete"
                    }
                },
                "required": ["folder_name"]
            }
        }
    }
]


user_input = input("You: ")

messages = [
    {
        "role": "user",
        "content": user_input
    }
]

# STEP 1: Ask AI what to do
response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen3:1.7b",
        "messages": messages,
        "tools": tools,
        "stream": False
    }
)


data = response.json()

assistant_message = data["message"]

print("\nAI decided:")

print(json.dumps(assistant_message, indent=2))


# STEP 2: Add AI's message to conversation
messages.append(assistant_message)


# STEP 3: Check whether AI requested a tool
tool_calls = assistant_message.get("tool_calls", [])


for tool_call in tool_calls:

    function_name = tool_call["function"]["name"]

    arguments = tool_call["function"]["arguments"]

    if function_name == "create_folder":

        folder_name = arguments["folder_name"]

        result = create_folder(folder_name)

        print("\nTool result:")
        print(result)


        # STEP 4: Send tool result back to AI
        messages.append(
            {
                "role": "tool",
                "content": result
            }
        )


# STEP 5: Ask AI for the final response
final_response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen3:1.7b",
        "messages": messages,
        "tools": tools,
        "stream": False
    }
)


final_data = final_response.json()


print("\nAI final response:")
print(final_data["message"]["content"])