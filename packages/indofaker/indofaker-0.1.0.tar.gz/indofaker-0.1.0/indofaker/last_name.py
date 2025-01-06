from indofaker import Religion, Tribe
from indofaker.base_name import BaseName


class LastName(BaseName):
    def __init__(self, name: str, religion: Religion, tribe: Tribe):
        super().__init__(name, religion, tribe)