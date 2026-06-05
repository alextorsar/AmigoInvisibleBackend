Feature: Manage Game with Admin Code
  As a game organizer
  I want to use my admin access code to manage the game
  So that I can verify the status and resend emails if any error occurred

  Scenario: Retrieve game status and player matchings
    Given a game exists with completed assignments
    When the organizer requests the game status using the valid admin access code
    Then the system should return the list of players and whether their emails were sent

  Scenario: Resend email to a specific player
    Given a game exists with completed assignments
    And the assignment for player "Alice" has email status as "failed"
    When the organizer requests to resend the email for "Alice" using the valid admin access code
    Then the system should attempt to send the email again
    And update the email status for "Alice" to "sent" on success

  Scenario: Update a player's email address
    Given a game exists with completed assignments
    When the organizer updates the email of player "Alice" to "new_alice@example.com" using the valid admin access code
    Then the system should update the email of player "Alice" to "new_alice@example.com"

  Scenario: Prevent access with invalid admin code
    Given a game exists
    When a user tries to access game management with an incorrect admin code
    Then the system should reject the request with an unauthorized error
