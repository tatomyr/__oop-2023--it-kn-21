from abc import ABC, abstractmethod

class Team(ABC):
    @abstractmethod
    def play(self):
        pass

class Barcelona(Team):
    def play(self):
        print("FC Barcelona is playing.")

class RealMadrid(Team):
    def play(self):
        print("Real Madrid is playing.")

class FootballFactory(ABC):
    @abstractmethod
    def create_team(self):
        pass

    def organize_game(self):
        team = self.create_team()
        team.play()

class BarcelonaFactory(FootballFactory):
    def create_team(self):
        return Barcelona()

class RealMadridFactory(FootballFactory):
    def create_team(self):
        return RealMadrid()

barcelona_factory = BarcelonaFactory()
barcelona_game = barcelona_factory.organize_game()

madrid_factory = RealMadridFactory()
madrid_game = madrid_factory.organize_game()
