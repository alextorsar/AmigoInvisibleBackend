Feature: Perform Secret Santa Draw
  As a game organizer
  I want to execute the Secret Santa draw
  So that every player is assigned a target friend and notified by email

  Scenario: Execute a successful draw
    Given a game with the following registered players:
      | Name   | Email               |
      | Alice  | alice@example.com   |
      | Bob    | bob@example.com     |
      | Charlie| charlie@example.com |
    And no draw has been performed yet
    When the organizer initiates the draw using the valid admin access code
    Then the system should generate matches for all players
    And every player must be assigned to exactly one receiver
    And no player can be assigned to themselves
    And every player must receive exactly one gift
    And the system should send personalized emails to all players
    And all assignments should be saved as completed

  Scenario: Attempt draw with insufficient players
    Given a game with only two registered players:
      | Name  | Email             |
      | Alice | alice@example.com |
      | Bob   | bob@example.com   |
    When the organizer tries to initiate the draw using the valid admin access code
    Then the system should reject the request
    And raise an invalid draw error stating there must be at least 3 players
