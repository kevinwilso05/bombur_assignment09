'''
Name: Mark Johnson 
email: johns8mk@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Collaborating using Git and OOP constructs
'''
from pip._internal import req
from PlayerPackage.PlayerClass import Player

class Team(): # Written by Mark Johnson
    def __init__(self, city, name, wins, players=None):
        self.checkCity(city)
        self.checkName(name)
        self.checkWins(wins)
        self.Players = list(players)
    def __repr__(self):
        return self.city + " " + self.name + ", " + str(self.wins)
    def __str__(self):
        return "The " + self.city + " " + self.name + " have " + str(self.wins) + " wins"
    
    #Team Name Methods
    def setTeamName(self, name):
        self.checkName(name)
    
    def checkName(self, name):
        if name == "Bengals":
            print ("Bengals is not a MLB team name.")
        else:
            self.name = name
            
    def getTeamName(self):
        return self.name
    
    # Team City Methods
    def getTeamCity(self):
        return self.city
    
    def setTeamCity(self, city):
        self.checkCity(city)
        
    def checkCity(self, city):
        if city == "Columbus":
            print ("This city does not have a MLB team.")
        else:
            self.city = city

    # Team Wins Methods        
    def getTeamWins(self):        
        return self.wins
    
    def setTeamWins(self, wins):
        self.checkWins(wins)
        
    def checkWins(self, wins):
        if wins < 0:
            print ("Wins cannot be less than zero. Not even the Reds are that bad.")
        else:
            self.wins = wins
    def addTeamWin(self, num):
        self.wins += num
        
    # Team Players Methods         
    def addPlayer(self, player):
        self.Players.append(player)
        
    def getPlayers(self):
        [player.getPlayer() for player in self.Players]
    # invokes the __repr__ dunder method in the player class
    
    def removePlayer(self, player):
        self.Players.remove(player)
        
        
    
