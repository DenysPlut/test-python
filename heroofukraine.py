class HeroOfUkraine():

    def __init__(self, name, level, honor, rank=10):
        """Initiate the hero with a default rank of 10"""
        self.name = name
        self.level = level
        self.honor = honor
        self.rank = rank  # Default rank set to 10 if not provided

    def show_heroOfUkraine(self):
        """Print all values"""
        description = (self.name + ' is honored with ' + str(self.level) +
                       ' medals for defending Ukraine against Russian conquerors ' +
                       self.honor + ' and he ranked with ' + str(self.rank)).title() + ' medals in total'
        print(description)

    def rank_up(self):
        """Upgrade the rank of Hero"""
        self.rank += 1

    def level_up(self):
        """Increase level by 3"""
        self.level += 3
        print(str(self.level) + ' highly endorsed')

    def move_up(self):
        """Moving"""
        print(self.name + ' is defending Ukraine from Russian aggressors')

    def set_rank(self, new_rank):
        """Set a new rank"""
        self.rank = new_rank
        print(str(self.rank) + ' promoted')