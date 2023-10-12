
class Player:
    def accept(self, visitor):
        pass

class LeagueOfLegendsPlayer(Player):
    def accept(self, visitor):
        visitor.visit_lol_player(self)

    def calculate_lol_rating(self):
        # Розрахунок рейтингу для гравця League of Legends
        return 1500  # Приклад розрахунку

class CounterStrikePlayer(Player):
    def accept(self, visitor):
        visitor.visit_cs_player(self)

    def calculate_cs_rating(self):
        # Розрахунок рейтингу для гравця Counter-Strike
        return 2000  # Приклад розрахунку

class Visitor:
    def visit_lol_player(self, lol_player):
        pass

    def visit_cs_player(self, cs_player):
        pass

class RatingCalculator(Visitor):
    def visit_lol_player(self, lol_player):
        rating = lol_player.calculate_lol_rating()
        print(f"League of Legends Player - Rating: {rating}")

    def visit_cs_player(self, cs_player):
        rating = cs_player.calculate_cs_rating()
        print(f"Counter-Strike Player - Rating: {rating}")

if __name__ == "__main":
    lol_player = LeagueOfLegendsPlayer()
    cs_player = CounterStrikePlayer()

    rating_calculator = RatingCalculator()

    lol_player.accept(rating_calculator)
    cs_player.accept(rating_calculator)
