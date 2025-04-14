import subprocess


class OllamaChat:
    def __init__(self, model_name="llama3.1"):
        self.model_name = model_name
        self.conversation_history = []
        self.process = None
        self.command = ['ollama', 'run', model_name]
        self.start_process()

    def start_process(self):
        self.process = subprocess.Popen(
            self.command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def get_process(self):
        return self.process

    def get_response(self, promt):
        output, error = self.process.communicate(input=promt, timeout=60)
        return output, error
