from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities import Assignment, Game, Player


class IGameRepository(ABC):
    """Interface for Game entity persistence operations."""

    @abstractmethod
    async def save(self, game: Game) -> Game:
        """Persist a new or modified Game entity."""
        pass

    @abstractmethod
    async def get_by_id(self, game_id: UUID) -> Game | None:
        """Retrieve a Game by its unique UUID database identifier."""
        pass

    @abstractmethod
    async def get_by_admin_code(self, admin_code: str) -> Game | None:
        """Retrieve a Game by its unique administrative access code."""
        pass


class IPlayerRepository(ABC):
    """Interface for Player entity persistence operations."""

    @abstractmethod
    async def save_all(self, players: list[Player]) -> list[Player]:
        """Persist a list of Player entities in batch."""
        pass

    @abstractmethod
    async def get_by_game_id(self, game_id: UUID) -> list[Player]:
        """Retrieve all Players participating in a specific game."""
        pass

    @abstractmethod
    async def get_by_id(self, player_id: UUID) -> Player | None:
        """Retrieve a Player by its unique UUID identifier."""
        pass


class IAssignmentRepository(ABC):
    """Interface for Assignment entity persistence operations."""

    @abstractmethod
    async def save_all(self, assignments: list[Assignment]) -> list[Assignment]:
        """Persist a list of Assignment entities in batch."""
        pass

    @abstractmethod
    async def save(self, assignment: Assignment) -> Assignment:
        """Persist a single Assignment entity (e.g., to update email status)."""
        pass

    @abstractmethod
    async def get_by_game_id(self, game_id: UUID) -> list[Assignment]:
        """Retrieve all Assignments matching giver-receiver pairs for a game."""
        pass

    @abstractmethod
    async def get_by_id(self, assignment_id: UUID) -> Assignment | None:
        """Retrieve a specific Assignment by ID."""
        pass
