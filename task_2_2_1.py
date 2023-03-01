class FcDinamo:
    def __init__(self, wins, draws, losses, goals_scored, goals_missed):
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_missed = goals_missed

    def add_result(self, scored, missed):
        if scored > missed:
            self.wins += 1
        elif scored == missed:
            self.draws += 1
        else:
            self.losses += 1
        self.goals_scored += scored
        self.goals_missed += missed

    def get_points(self):
        return self.wins * 3 + self.draws

    def get_goal_difference(self):
        return self.goals_scored - self.goals_missed


class TotalGames(FcDinamo):
    def __init__(self, wins, draws, losses, goals_scored, goals_missed):
        super().__init__(wins, draws, losses, goals_scored, goals_missed)
        self.total_games = wins + draws + losses

    def add_result(self, scored, missed):
        super().add_result(scored, missed)
        self.total_games += 1

    def get_total_games(self):
        return self.total_games


if __name__ == "__main__":
    team = FcDinamo(0, 0, 0, 0, 0)
    team.add_result(2, 3)
    team.add_result(1, 4)
    team.add_result(0, 3)

    print(f"Points: {team.get_points()}, Goal difference: {team.get_goal_difference()}")

    team = TotalGames(0, 0, 0, 0, 0)
    team.add_result(3, 0)
    print(f"Total games: {team.get_total_games()}")
