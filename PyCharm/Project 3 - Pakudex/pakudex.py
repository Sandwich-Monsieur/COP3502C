from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if self.pakuri_list == []:
            return None
        return [p.get_species() for p in self.pakuri_list]

    def get_stats(self, species):
        for p in self.pakuri_list:
            if p.get_species() == species:
                return [p.get_attack(), p.get_defense(), p.get_speed()]
            """else:
                return None"""

    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda p: p.get_species())

    def add_pakuri(self, species):
        if self.get_size() < self.capacity:
            if self.get_species_array() is not None and species in self.get_species_array():
                return False
            self.pakuri_list.append(Pakuri(species))
            return True
        else:
            return False

    def evolve_species(self, species):
        for p in self.pakuri_list:
            if p.get_species() == species:
                p.evolve()
                return True
        return False
