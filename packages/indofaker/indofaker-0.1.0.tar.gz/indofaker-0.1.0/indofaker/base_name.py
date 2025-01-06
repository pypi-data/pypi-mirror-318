from abc import ABC, abstractmethod

from indofaker import Religion, Tribe
from indofaker.gender import Gender


class BaseName():
    def __init__(self, name: str, gender:Gender, religion: Religion, tribe: Tribe):
        self.name = name
        self.religion = religion
        self.tribe = tribe
        self.gender = gender


