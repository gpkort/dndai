from enum import Enum

ABILITY_SCORE_LOOKUP = {
    3: -0.2, 4: -0.2, 5: -0.2,
    6: -0.1, 7: -0.1, 8: -0.1,
    9: 0, 9: 0, 9: 0, 9: 0,
}

class ATTACK_TYPES(Enum):
    DEATH_RAY_POISON = 0,
    MAGIC_WANDS = 1,
    PARALYSIS_STONE = 2,
    DRAGON_BREATH = 3,
    RODS_STAFF_SPELLS = 4

