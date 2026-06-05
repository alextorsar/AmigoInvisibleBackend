from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from src.domain.entities import Game, Player, Assignment

class IGameRepository(ABC):
    """Interface for Game entity persistence operations."""

    @abstractmethod
    async def save(self, game: Game) -> Game:
        """Persist a new or modified Game entity."""
        pass

    @abstractmethod
    async def get_by_id(self, game_id: UUID) -> Optional[Game]:
        """Retrieve a Game by its unique UUID database identifier."""
        pass

    @abstractmethod
    async def get_by_admin_code(self, admin_code: str) -> Optional[Game]:
        """Retrieve a Game by its unique administrative access code."""
        pass


class IPlayerRepository(ABC):
    """Interface for Player entity persistence operations."""

    @abstractmethod
    async def save_all(self, players: List[Player]) -> List[Player]:
        """Persist a list of Player entities in batch."""
        pass

    @abstractmethod
    async def get_by_game_id(self, game_id: UUID) -> List[Player]:
        """Retrieve all Players participating in a specific game."""
        pass

    @abstractmethod
    async def get_by_id(self, player_id: UUID) -> Optional[Player]:
        """Retrieve a Player by its unique UUID identifier."""
        pass


class IAssignmentRepository(ABC):
    """Interface for Assignment entity persistence operations."""

    @abstractmethod
    async def save_all(self, assignments: List[Assignment]) -> List[Assignment]:
        """Persist a list of Assignment entities in batch."""
        pass

    @abstractmethod
    async def save(self, assignment: Assignment) -> Assignment:
        """Persist a single Assignment entity (e.g., to update email status)."""
        pass

    @abstractmethod
    async def get_by_game_id(self, game_id: UUID) -> List[Assignment]:
        """Retrieve all Assignments matching giver-receiver pairs for a game."""
        pass

    @abstractmethod
    async def get_by_id(self, assignment_id: UUID) -> Optional[Assignment]:
        """Retrieve a specific Assignment by ID."""
        pass
