import subprocess
import json
from ollama_chat import OllamaChat

from util import create_directory, delete_directory, list_directories, rename_directory

SYSTEM_PROMPT = """
From now on, always respond in the following JSON format:

There are 4 types of folder processes:
1. Create a folder
2. Delete a folder
3. List folders
4. Rename a folder

Process keywords:
- If the user mentions creating a folder, set "process" to "create"
- If the user mentions deleting a folder, set "process" to "delete"
- If the user mentions listing folders, set "process" to "list"
- If the user mentions renaming a folder, set "process" to "rename"

If any of these processes are identified, include the folder name in the "data" section. If not, leave the "data" field as an empty object. The "data" should always be a JSON object.

### Examples:

User says: "Create a folder named folder1"
Response:
{
  "response": "Creating folder 'folder1'.",
  "data": {
    "process": "create",
    "folder_name": "folder1"
  }
}

User says: "Delete folder1"
Response:
{
  "response": "Deleting folder 'folder1'.",
  "data": {
    "process": "delete",
    "folder_name": "folder1"
  }
}

User says: "Show me all folders"
Response:
{
  "response": "Listing all folders.",
  "data": {
    "process": "list"
  }
}

User says: "Rename folder1 to folder2"
Response:
{
  "response": "Renaming folder1 to folder2.",
  "data": {
    "process": "rename",
    "old_name": "folder1",
    "folder_name": "folder2"
  }
}

If the input does not contain any folder-related command, return:
{
  "response": "No folder action detected.",
  "data": {}
}
"""


def run_ollama_and_get_output(user_input, model_name="llama3.1"):
    ollama_chat = OllamaChat()
    process = ollama_chat.get_process()

    full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:"

    try:
        output, error = ollama_chat.get_response(promt=full_prompt)
        output_obj = json.loads(output)
        folder_name = ""
        if 'folder_name' in output_obj['data']:
            folder_name = output_obj['data']['folder_name']

        print(f"Folder name: {folder_name}")

        if 'process' in output_obj['data']:
            process_type = output_obj['data']['process']
            if process_type == "create":
                create_directory(folder_name)
            elif process_type == "delete":
                delete_directory(folder_name)
                pass
            elif process_type == "list":
                list_directories(folder_name='')
                pass
            elif process_type == "rename":
                old_name = output_obj['data'].get('old_name')
                pass

    except subprocess.TimeoutExpired:
        process.kill()
        output, error = process.communicate()

    return output.strip(), process.pid


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        response, pid = run_ollama_and_get_output(user_input)
        print(f"(PID: {pid}) LLaMA: {response}")
