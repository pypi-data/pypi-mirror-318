from enum import Enum

from indofaker import Religion, Tribe
from indofaker.base_name import BaseName
from indofaker.gender import Gender


class FirstName(BaseName):
    def __init__(self, name: str,gender:Gender, religion: Religion, tribe: Tribe):
        super().__init__(name, gender, religion, tribe)





class FirstNames(Enum):

    # ALL, ALL, ALL

    TRI = FirstName("Tri", Gender.ALL, Religion.ALL, Tribe.ALL)
    NUR = FirstName("Nur", Gender.ALL, Religion.ALL, Tribe.ALL)



    # MALE, ALL, ALL

    AGUS = FirstName("Agus", Gender.MALE, Religion.ALL, Tribe.ALL)
    BUDI = FirstName("Budi", Gender.MALE, Religion.ALL, Tribe.ALL)
    DEDI = FirstName("Dedi", Gender.MALE, Religion.ALL, Tribe.ALL)
    EKO = FirstName("Eko", Gender.MALE, Religion.ALL, Tribe.ALL)
    FIRMAN = FirstName("Firman", Gender.MALE, Religion.ALL, Tribe.ALL)
    HADI = FirstName("Hadi", Gender.MALE, Religion.ALL, Tribe.ALL)
    JOKO = FirstName("Joko", Gender.MALE, Religion.ALL, Tribe.ALL)
    KARTO = FirstName("Karto", Gender.MALE, Religion.ALL, Tribe.ALL)
    MARDI = FirstName("Mardi", Gender.MALE, Religion.ALL, Tribe.ALL)
    PURWADI = FirstName("Purwadi", Gender.MALE, Religion.ALL, Tribe.ALL)
    SURYA = FirstName("Surya", Gender.MALE, Religion.ALL, Tribe.ALL)
    WIJAYA = FirstName("Wijaya", Gender.MALE, Religion.ALL, Tribe.ALL)
    YUDHA = FirstName("Yudha", Gender.MALE, Religion.ALL, Tribe.ALL)
    ZUL = FirstName("Zul", Gender.MALE, Religion.ALL, Tribe.ALL)

    # FEMALE, ALL, ALL

    AYU = FirstName("Ayu", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    INDAH = FirstName("Indah", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    LESTARI = FirstName("Lestari", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    FITRI = FirstName("Fitri", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    DEWI = FirstName("Dewi", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    SRI = FirstName("Sri", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    RINI = FirstName("Rini", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    YANTI = FirstName("Yanti", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    SANTI = FirstName("Santi", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    LINA = FirstName("Lina", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    OKTA = FirstName("Okta", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    RATNA = FirstName("Ratna", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    KARTINI = FirstName("Kartini", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    WULAN = FirstName("Wulan", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    GITA = FirstName("Gita", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    ANISA = FirstName("Anisa", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    MEGA = FirstName("Mega", Gender.FEMALE, Religion.ALL, Tribe.ALL)
    LIA = FirstName("Lia", Gender.FEMALE, Religion.ALL, Tribe.ALL)







