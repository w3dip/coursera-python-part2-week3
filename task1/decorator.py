from abc import ABC, abstractmethod

class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.stats = {}
        self.positive_effects = []
        self.negative_effects = []

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        self.positive_effects = super().get_positive_effects()
        self.positive_effects.append(self.__class__.__name__)
        return self.positive_effects


class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        self.negative_effects = super().get_negative_effects()
        self.negative_effects.append(self.__class__.__name__)
        return self.negative_effects


class Berserk(AbstractPositive):
    def get_stats(self):
        self.stats = self.base.get_stats()
        for key in ["Strength", "Endurance", "Agility", "Luck"]:
            self.stats[key] += 7
        for key in ["Perception", "Charisma", "Intelligence"]:
            self.stats[key] -= 3
        self.stats['HP'] += 50
        return self.stats


class Blessing(AbstractPositive):
    def get_stats(self):
        self.stats = self.base.get_stats()
        for key in ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]:
            self.stats[key] += 2
        return self.stats


class Weakness(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        for key in ["Strength", "Endurance", "Agility"]:
            self.stats[key] -= 4
        return self.stats


class Curse(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        for key in ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]:
            self.stats[key] -= 2
        return self.stats


class EvilEye(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        for key in ["Luck"]:
            self.stats[key] -= 10
        return self.stats