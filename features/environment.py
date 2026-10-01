from pages.notes_page import NotesPage


def before_all(context):
    context.base_url = "http://127.0.0.1:8000"
    context.page = NotesPage(context.base_url)