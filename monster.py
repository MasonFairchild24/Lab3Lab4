from pydantic import BaseModel
from typing import List, Optional

class Action(BaseModel):
    name: str
    damage_dice: Optional[List[str]] = None
    dc_type: Optional[str] = None
    dc_value: Optional[int] = None


class Monster(BaseModel):
    name: str
    hit_points: int
    armor_class: int
    challenge_rating: float
    actions: List[Action]
