from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import UUID


@dataclass
class Player:
    """
    Domain entity representing a player participating in a Secret Santa game.
    All properties and comments are in English.
    """

    id: UUID | None
    game_id: UUID
    name: str
    email: str


@dataclass
class Game:
    """
    Domain entity representing a Secret Santa game event.
    """

    id: UUID | None
    admin_code: str
    name: str
    budget_limit: float | None
    event_date: date
    email_subject: str
    email_body: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    players: list[Player] = field(default_factory=list)


@dataclass
class Assignment:
    """
    Domain entity representing a Secret Santa assignment
    where a giver is matched to a receiver.
    """

    id: UUID | None
    game_id: UUID
    giver_id: UUID
    receiver_id: UUID
    email_sent: bool = False
    sent_at: datetime | None = None
