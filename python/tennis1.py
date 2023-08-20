# -*- coding: utf-8 -*-

class TennisGame1:

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
        if self.p1points == self.p2points:
            if self.p1points >= 3:
                return "Deuce"
            else:
                return self.pointNames[self.p1points] + "-All"

        leader = None
        leader_score = None
        loser_score = None

        if self.p1points > self.p2points:
            leader = self.player1Name
            leader_score = self.p1points
            loser_score = self.p2points
        else:
            leader = self.player2Name
            leader_score = self.p2points
            loser_score = self.p1points

        if leader_score >= 4:
            if leader_score - loser_score > 1:
                return f"Win for {leader}"
            else:
                return f"Advantage {leader}"

        return self.pointNames[self.p1points] +\
            f"-{self.pointNames[self.p2points]}"
