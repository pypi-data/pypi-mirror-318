import random

from indofaker.base_name import BaseName
from indofaker.family_name import FamilyNames, FamilyName
from indofaker.first_name import FirstNames, FirstName
from indofaker.gender import Gender



def my_filter(name:BaseName):
    return name.gender == Gender.MALE



def name_generator():


    #first_name_list : list[FirstName] = list(FirstNames)
    #filtered_first_name =  list(filter(my_filter, first_name_list))

    first_name : FirstName = random.choice(list(FirstNames))
    family_name : FamilyName = random.choice(list(FamilyNames))

    return f"{first_name.name} {family_name.name}"

