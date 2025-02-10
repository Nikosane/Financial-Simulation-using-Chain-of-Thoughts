import requests

class DeepseekClient:
    def __init__(self, model="deepseek-r1"):
        self.url = "http://localhost:11434/api/generate"  # Adjust if needed
        self.model = model

    def query(self, prompt):
        data = {"model": self.model, "prompt": prompt}
        response = requests.post(self.url, json=data)
        return response.json().get("response", "").strip()
