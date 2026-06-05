Feature: Secret Santa Game Creation
  As a game organizer
  I want to create a new Secret Santa game
  So that I can manage players and perform a draw

  Scenario: Successfully create a new game
    Given the organizer provides valid game details:
      | Name          | Budget Limit | Event Date | Email Subject   | Email Body                                             |
      | Family Dinner | 20.00        | 2026-12-25 | Secret Santa 2026 | Hello {giver}, you are giving a gift to {receiver}! |
    When the organizer submits the creation request
    Then a new game should be registered in the database
    And a unique 8-character admin access code should be generated
    And the game details should be saved successfully
