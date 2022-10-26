'''
Name: Mark Johnson 
email: johns8mk@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Collaborating using Git and OOP constructs
'''
from pip._internal import req

class Team(): # Written by Mark Johnson
    def teamName(self, name):
        self.checkName(name)
    def checkName(self, name):
        if name == "Bengals":
            print ("Bengals is not a MLB team name.")
        else:
            self.name = name
    def teamCity(self, city):
        self.checkCity(city)
    def checkCity(self, city):
        if city == "Columbus":
            print ("This city does not have a MLB team.")
        else:
            self.city = city
    def teamWins(self, wins):
        self.checkWins(wins)
    def checkWins(self, wins):
        if wins < 0:
            print ("Wins cannot be less than zero. Not even the Reds are that bad.")
        else:
            self.wins = wins
    def __init__(self, city, name, wins):
        self.checkCity(city)
        self.checkName(name)
        self.checkWins(wins)
    def __repr__(self):
        return self.city + " " + self.name + ", " + str(self.wins)
    def __str__(self):
        return self.city + " " + self.name + ", " + str(self.wins) + " wins"
