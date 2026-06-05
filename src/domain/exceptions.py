class DomainException(Exception):
    """Base exception for all domain-related errors."""

    pass


class GameNotFoundException(DomainException):
    """Raised when a Secret Santa game cannot be found."""

    def __init__(self, game_id_or_code: str):
        super().__init__(
            f"Secret Santa game with ID or code '{game_id_or_code}' was not found."
        )


class PlayerNotFoundException(DomainException):
    """Raised when a player cannot be found."""

    def __init__(self, player_id: str):
        super().__init__(f"Player with ID '{player_id}' was not found.")


class DuplicatePlayerEmailException(DomainException):
    """Raised when a player with the same email already exists in the same game."""

    def __init__(self, email: str):
        super().__init__(
            f"A player with email '{email}' is already registered in this game."
        )


class InvalidAdminCodeException(DomainException):
    """Raised when the provided admin code is incorrect."""

    def __init__(self):
        super().__init__("The provided administrative access code is invalid.")


class InvalidGameDrawException(DomainException):
    """Raised when the conditions for performing a draw are not met."""

    def __init__(self, reason: str):
        super().__init__(f"Cannot perform Secret Santa draw: {reason}")


class DrawAlreadyPerformedException(DomainException):
    """Raised when trying to perform a draw on a game that already has assignments."""

    def __init__(self, game_id: str):
        super().__init__(f"Draw has already been performed for game '{game_id}'.")
