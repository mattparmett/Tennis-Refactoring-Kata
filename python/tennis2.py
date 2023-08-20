# -*- coding: utf-8 -*-

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.pointNames = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        # Handle tie case
        if self.p1points == self.p2points:
            if self.p1points < 3:
                return self.pointNames[self.p1points] + "-All"
            else:
                return "Deuce"

        if self.p1points > 3 or self.p2points > 3:
            # Handle win case
            if abs(self.p1points - self.p2points) > 1:
                if self.p1points > self.p2points:
                    return f"Win for {self.player1Name}"
                else:
                    return f"Win for {self.player2Name}"

            # Handle advantage case
            if self.p1points > self.p2points:
                return f"Advantage {self.player1Name}"
            else:
                return f"Advantage {self.player2Name}"

        # Handle normal score case
        P1res = self.pointNames[self.p1points]
        P2res = self.pointNames[self.p2points]
        return f"{P1res}-{P2res}"
