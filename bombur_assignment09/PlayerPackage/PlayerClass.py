'''
Name: Kevin, Wilson, Mark Johnson, Brett Perez
email: perezbd@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: In this project, we use Classes and OOP to create a simple, informational program.
Citations: 
Anything else that's relevant: 
'''

# Code written by Brett Perez
class Player():
    def __init__(self, name, runs):
        self.name = name
        self.runs = runs
        
    def __repr__(self):
        return "name = " + self.name + ", runs = " + str(self.runs)
    
    def __str__(self):
        return self.name + " has " + str(self.runs) + " runs!"
    
    def setName (self, name):
        self.name = name
        
    def getName (self):
        return self.name
    
    def setRuns (self, runs):
        self.runs = runs
        
    def getRuns (self):
        return self.runs
    
    # Add total runs made a player once a game is complete.
    def newRun (self, x):
        self.runs += x
        return str(x) + " runs logged. " + "Runs now = " + str(self.runs)
