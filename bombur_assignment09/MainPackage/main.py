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

from PlayerPackage.PlayerClass import Player
from TeamPackage.TeamClass import Team


# Create Players for the Reds Team 
RedsP1 = Player("Chase Anderson", 5)
RedsP2 = Player("Luis Cessa", 30)
RedsP3 = Player("Fernando Cruz", 50)
RedsP4 = Player("Justin Dunn",37)
RedsP5 = Player("Joey Votto", 61)

# Create Players for the Cubs Team 

CubsP1 = Player("David Bote", 80)
CubsP2 = Player("Zach McKinstry", 62)
CubsP3 = Player("Alfonso Rivas", 34)
CubsP4 = Player("Jared Young", 50)
CubsP5 = Player("David Bote", 68)

# Create Reds team with Players 
reds = Team("Cincinnati", "Reds", 56, [RedsP1, RedsP2, RedsP3, RedsP4, RedsP5])

# Create Cubs Team with Players
cubs = Team("Chicago", "Cubs", 100, [CubsP1, CubsP2, CubsP3, CubsP4, CubsP5])

# Initiate Teams Array 
teams = [cubs, reds]

# Print Teams Information with str dunder method
[print(team.__str__()) for team in teams] 

# Get team name and city with list comprehension for fun    
[print(f"The {team.getTeamName()} play in {team.getTeamCity()}") for team in teams]

# Get Reds players - invokes player __repr__ method through team.getplayers method
print("\n" + "The Reds Players are:")
reds.getPlayers()

# Get Reds players
print("\n" + "The Cubs Players are:")
reds.getPlayers()

# Add a new player to reds 

RedsP6 = Player("Kyle Farmer", 67)
reds.addPlayer(RedsP6)

# Adding Players to the Cubs
CubsP6 = Player("Patrick Wisdom", 89)
cubs.addPlayer(CubsP6)

print(RedsP1.getName())

# Setting reds name 
reds.setTeamName("RedLegs")
print(f"The Reds name has been changed to the {reds.getTeamName()}")

# Collect total reds runs 
redsRuns = 0
for player in reds.Players:
    redsRuns += player.runs

print(f"The {reds.getTeamName()} have {redsRuns} runs so far this season")

# Removes player from the reds 
reds.removePlayer(RedsP2)

# Add some runs 
print(RedsP3.newRun(15))

# Invoking __str__ method in players 
[print(player.__str__()) for player in reds.Players]
    
# Uses setTeamCity method 
cubs.setTeamCity("Orlando")
#Prints change
print(cubs.getTeamCity())

# Uses getTeamWinsMethod
print(cubs.getTeamWins())

# Uses addTeamWin
reds.addTeamWin(5)

# Sets PlayerName
CubsP4.setName("Jonathan Doe")

# Gets Player 6 name
print(RedsP6.getName())

# Gets Player runs 

[print(player.getRuns()) for player in cubs.Players]



    
    








 





