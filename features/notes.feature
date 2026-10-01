Feature: Notes API

  Scenario: Successfully create a note
    Given a valid note payload
    When I send a request to create the note
    Then the response status code should be 200
    And the response should contain the correct title

  Scenario: Fail to create a note with invalid data
    Given an invalid note payload
    When I send a request to create the note
    Then the response status code should be 422

  Scenario: Get all notes when there are notes
    Given there is at least one note
    When I request all notes
    Then the response status code should be 200
    And the response should be a list

  Scenario: Get all notes when there are no notes
    Given there are no notes
    When I request all notes
    Then the response status code should be 200
    And the response should be an empty list

  Scenario: Get a note by valid id
    Given there is at least one note
    When I request the note by its id
    Then the response status code should be 200
    And the response should contain the correct title

  Scenario: Get a note by invalid id
    When I request the note with id 999999
    Then the response status code should be 404

  Scenario: Update a note by valid id
    Given there is at least one note
    When I update the note with new data
    Then the response status code should be 200
    And the response should contain the new title

  Scenario: Update a note by invalid id
    When I update the note with id 999999
    Then the response status code should be 404

  Scenario: Delete a note by valid id
    Given there is at least one note
    When I delete the note by its id
    Then the response status code should be 200

  Scenario: Delete a note by invalid id
    When I delete the note with id 999999
    Then the response status code should be 404