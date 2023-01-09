import csv
import numpy as np
import pandas as pan
import matplotlib.pyplot as plt

list_of_animals = [] # Contains list of all animal objects

#TODO: Create animal class object that creates animal with properties
class Animal:
    def __init__(self, category, scientific_name, common_names, conservation_status='', park_name='', observations=''):
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
with open("python/Biodiversity_National_Park/observations.csv", 'r') as observations:
    with open("python/Biodiversity_National_Park/species_info.csv", 'r') as species_info:
        dict_reader_species = csv.DictReader(species_info)
        dict_reader_obsvr = csv.DictReader(observations)
        list_of_animals_counter = 0

        for row1 in dict_reader_species:
            list_of_animals.append(Animal(category=row1['category'], scientific_name=row1['scientific_name'], common_names=row1['common_names'], conservation_status=row1['conservation_status']))
            
            for row in dict_reader_obsvr:
                if row1['scientific_name'] == row['scientific_name']:
                    
                    list_of_animals[list_of_animals_counter].park_name = row['park_name']
                    list_of_animals[list_of_animals_counter].observations = row['observations']
                    list_of_animals_counter += 1
                    break

