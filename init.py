import subprocess
import json

from util import create_directory, delete_directory, list_directories, rename_directory

SYSTEM_PROMPT = """
From now on, always answer in JSON format like this:

There are 4 type of folder process:
1. Create a folder
2. Delete a folder
3. List folders
4. Rename a folder

If user say create process = create, 
if user say delete a folder process equals = delete 
If user say list process = list, 
if user say rename process equals = rename 

if are there any process like (create,delete,list,rename) , put the folder name in the data section, otherwise let the data be empty. data should be a JSON object with the following structure:

example: create a folder
  "data": {
    "process": "create",
    "folder_name": "folder1"
  }
expampler: delete a folder
    "data": {
        "process": "delete",
        "folder_name": "folder1"
    }

{
  "response": "<your answer>",
  "data": "<any additional data if needed>"
}
"""


def run_ollama_and_get_output(user_input, model_name="llama3.1"):
    full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:"

    command = ["ollama", "run", model_name]
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    try:
        output, error = process.communicate(input=full_prompt, timeout=60)

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
