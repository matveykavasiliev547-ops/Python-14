import requests

class NotesAPIClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url

    def get_notes(self) -> list[dict]:
        response = requests.get(f"{self.base_url}/notes")
        response.raise_for_status()
        return response.json()

    def add_note(self, content: str) -> dict:
        response = requests.post(f"{self.base_url}/notes", json={"content": content})
        response.raise_for_status()
        return response.json()

    def update_note(self, note_id: int, content: str) -> dict:
        response = requests.put(f"{self.base_url}/notes/{note_id}", json={"content": content})
        response.raise_for_status()
        return response.json()

    def delete_note(self, note_id: int) -> dict:
        response = requests.delete(f"{self.base_url}/notes/{note_id}")
        response.raise_for_status()
        return response.json()