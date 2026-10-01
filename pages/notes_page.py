import requests


class NotesPage:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def create_note(self, payload):
        return self.session.post(f"{self.base_url}/notes", json=payload)

    def get_all_notes(self):
        return self.session.get(f"{self.base_url}/notes")

    def get_note(self, note_id):
        return self.session.get(f"{self.base_url}/notes/{note_id}")

    def update_note(self, note_id, payload):
        return self.session.put(f"{self.base_url}/notes/{note_id}", json=payload)

    def delete_note(self, note_id):
        return self.session.delete(f"{self.base_url}/notes/{note_id}")