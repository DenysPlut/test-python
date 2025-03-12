
class HeroOfUkraine():

    def __init__(self,name,level,honor, rank):
        """Initiate the hero"""
        self.name = name
        self.level = level
        self.honor = honor
        self.rank = rank

    def show_heroOfUkraine(self):
        """Print all values"""
        description = (self.name + ' is honored with ' + str(self.level) + ' medals for defending Ukraine against Russian conquerors ' + self.honor + ' and he ranked with ' + str(self.rank)).title() + ' medals in total'
        print(description)

    def rank_up(self):
        """Upgrade the level of Hero"""
        self.rank += 1

    def move_up(self):
        """Moving"""
        print(self.name + ' is defending Ukraine from Russian aggressors')
    def set_rank(self, new_rank):
        self.rank = new_rank