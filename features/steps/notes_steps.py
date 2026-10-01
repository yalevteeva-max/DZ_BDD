from behave import given, when, then
from factories.note_factory import NoteFactory


@given('a valid note payload')
def step_valid_payload(context):
    context.payload = NoteFactory.valid_note()


@given('an invalid note payload')
def step_invalid_payload(context):
    context.payload = NoteFactory.invalid_note()


@given('there is at least one note')
def step_create_note(context):
    context.payload = NoteFactory.valid_note()
    context.response = context.page.create_note(context.payload)
    context.note_id = context.response.json()['id']


@given('there are no notes')
def step_clear_notes(context):
    response = context.page.get_all_notes()
    for note in response.json():
        context.page.delete_note(note['id'])


@when('I send a request to create the note')
def step_create(context):
    context.response = context.page.create_note(context.payload)


@when('I request all notes')
def step_get_all(context):
    context.response = context.page.get_all_notes()


@when('I request the note by its id')
def step_get_by_id(context):
    context.response = context.page.get_note(context.note_id)


@when('I request the note with id {note_id:d}')
def step_get_by_invalid_id(context, note_id):
    context.response = context.page.get_note(note_id)


@when('I update the note with new data')
def step_update(context):
    context.payload = NoteFactory.valid_note()
    context.response = context.page.update_note(context.note_id, context.payload)


@when('I update the note with id {note_id:d}')
def step_update_invalid(context, note_id):
    context.response = context.page.update_note(note_id, NoteFactory.valid_note())


@when('I delete the note by its id')
def step_delete(context):
    context.response = context.page.delete_note(context.note_id)


@when('I delete the note with id {note_id:d}')
def step_delete_invalid(context, note_id):
    context.response = context.page.delete_note(note_id)


@then('the response status code should be {status_code:d}')
def step_status_code(context, status_code):
    assert context.response.status_code == status_code


@then('the response should contain the correct title')
def step_correct_title(context):
    data = context.response.json()
    assert data['title'] == context.payload['title']


@then('the response should contain the new title')
def step_new_title(context):
    data = context.response.json()
    assert data['title'] == context.payload['title']


@then('the response should be a list')
def step_is_list(context):
    data = context.response.json()
    assert isinstance(data, list)


@then('the response should be an empty list')
def step_is_empty_list(context):
    data = context.response.json()
    assert isinstance(data, list)
    assert len(data) == 0