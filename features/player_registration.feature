Feature: Player Registration
  As a game organizer
  I want to register players to a Secret Santa game
  So that they can participate in the draw

  Scenario: Successfully register multiple players to a game
    Given a created game exists
    When the organizer adds the following players:
      | Name   | Email               |
      | Alice  | alice@example.com   |
      | Bob    | bob@example.com     |
      | Charlie| charlie@example.com |
    Then all players should be registered to the game
    And no assignments should exist yet

  Scenario: Prevent registering duplicate player emails in the same game
    Given a created game exists
    And a player with email "alice@example.com" is already registered
    When the organizer tries to add a player named "Alice Clone" with email "alice@example.com"
    Then the system should reject the player registration
    And raise a duplicate email error

  Scenario: Prevent registering duplicate player names in the same game
    Given a created game exists
    And a player with name "Alice" is already registered
    When the organizer tries to add a player named "Alice" with email "another_alice@example.com"
    Then the system should reject the player registration
    And raise a duplicate name error

