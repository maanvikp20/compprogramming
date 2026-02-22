# 4 kyu - The Greatest Warrior

class Warrior:
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []

    def training(self, training_data):
        if training_data[2] > self.level:
            return "Not strong enough"

        self.achievements.append(training_data[0])
        self.experience += training_data[1]
        self.checkMaxes()
        self.level = self.experience // 100
        self.rank = self.getRank()
        return training_data[0]

    def battle(self, enemy_level):
        if enemy_level < 1 or enemy_level > 100:
            return "Invalid level"

        level_diff = enemy_level - self.level
        self_rank_index = self.level // 10
        enemy_rank_index = enemy_level // 10

        if level_diff == 0:
            self.experience += 10
            result = "A good fight"

        elif level_diff == -1:
            self.experience += 5
            result = "A good fight"

        elif level_diff <= -2:
            return "Easy fight"

        else:
            if level_diff >= 5 and enemy_rank_index > self_rank_index:
                return "You've been defeated"

            self.experience += 20 * level_diff * level_diff
            result = "An intense fight"

        self.checkMaxes()
        self.level = self.experience // 100
        self.rank = self.getRank()

        return result

    def getRank(self, level=None):
        if level is None:
            level = self.level

        ranks = [
            "Pushover", "Novice", "Fighter", "Warrior",
            "Veteran", "Sage", "Elite", "Conqueror",
            "Champion", "Master", "Greatest"
        ]

        return ranks[level // 10]

    def checkMaxes(self):
        if self.experience > 10000:
            self.experience = 10000
        if self.experience < 0:
            self.experience = 0

bruce_lee = Warrior()
print(bruce_lee.level)         # => 1
print(bruce_lee.experience)    # => 100
print(bruce_lee.rank)          # => "Pushover"
print(bruce_lee.achievements)  # => []
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1])) # => "Defeated Chuck Norris"
print(bruce_lee.experience)    # => 9100
print(bruce_lee.level)         # => 91
print(bruce_lee.rank)          # => "Master"
print(bruce_lee.battle(90))    # => "A good fight"
print(bruce_lee.experience)    # => 9105
print(bruce_lee.achievements)  # => ["Defeated Chuck Norris"]