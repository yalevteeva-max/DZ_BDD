import random
import string


class NoteFactory:
    def valid_note():
        return {"title": "Test Note", "content": "This is a test note"}

    def random_note():
        title = ''.join(random.choices(string.ascii_letters, k=10))
        content = ''.join(random.choices(string.ascii_letters, k=30))
        return {"title": title, "content": content}

    def invalid_note():
        return {"content": "No title here"}