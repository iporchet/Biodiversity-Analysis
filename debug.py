import numpy as np
import pandas as pan
import matplotlib.pyplot as plt

list_of_animals = [] # Contains list of all animal objects

#TODO: Create animal class object that creates animal with properties
class Animal:
    def __init__(self, category, scientific_name, common_names, conservation_status, park_name, observations):
        self.category = category
        self.scientific_name = scientific_name
        self.common_names = common_names
        self.conservation_status = conservation_status
        self.park_name = park_name
        self.observations = observations

    def get_category(self):
        return self.category

    def get_conservation_status(self):
        return self.conservation_status

    def get_observations(self):
        return self.observations




# reading csv file to obtain attributes to create animal class
with open("python/Biodiversity_National_Park/species_info.csv", 'r') as species_info:
    for x in species_info:
        if "category,scientific_name" in x:
            pass
        else:
            if x.count("\"") == 2:
                common_names = []
                new_animal = list(x.split(','))

                for y in new_animal:
                    if y[0] == "\"":
                        indx1 = new_animal.index(y)

                common_names.append(new_animal[indx1][1:])

                for y in range(indx1+1, len(new_animal)):
                    if "\"" in new_animal[y] and y != indx1:
                        common_names.append(new_animal[y][:-1])
                        break

                    else:
                        common_names.append(new_animal[y])

                print(common_names)
            

            else:
                new_animal = list(x.split(','))