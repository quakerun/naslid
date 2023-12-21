class FootballPlayer:
    def init(self, country, running_speed, jumping_height):
        self.country = country
        self.running_speed = running_speed
        self.jumping_height = jumping_height

    def information(self):
        print(f"Football player from {self.country}, his running speed is {self.running_speed} and jumping height is {self.jumping_height}")


class Goalkeeper(FootballPlayer):
    def init(self, country, running_speed, jumping_height, hand_width):
        super().init(country, running_speed, jumping_height)
        self.hand_width = hand_width

    def information(self):
        print(f"Football player from {self.country}, his running speed is {self.running_speed}, jumping height is {self.jumping_height}, and hand width is {self.hand_width}")


f1 = FootballPlayer("Italy", 7, 67)
f1.information()
f2 = Goalkeeper("France", 5, 72, 207)
f2.information()
