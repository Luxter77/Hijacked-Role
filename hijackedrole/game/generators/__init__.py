from typing import List

import random

import hijackedrole.game.classes.lizzards_and_oubliettes as l_n_o
import hijackedrole.game.classes.margaret_and_joshua as m_n_j

from hijackedrole.game.characters import NPC, PlayerCharacter
from hijackedrole.game import InGameObject
from hijackedrole.game.mechanics import Encounter

def generate_random_NPC() -> NPC:
    ...

def generate_important_random_NPC() -> NPC:
    ...

def generate_player_character() -> PlayerCharacter:
    ...

def generate_random_encounter() -> Encounter:
    ...

def loot_generator() -> List[InGameObject]:
    ...
