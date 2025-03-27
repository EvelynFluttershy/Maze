from classes import *
from functions import *

# här initieras värden #
clear() # för att tömma skärmen när spelet först startar
print(" name your character:")
var = input()
player = Player(50, 50, var) # skapar ett objekt för spelaren
terrain = [
	Terrain(45, 51, "tree"),
	Terrain(47, 52, "tree"),
	Terrain(48, 44, "tree"),
	Terrain(49, 55, "tree"),
	Terrain(53, 46, "tree")
]
pickup = [
	Pickup(52, 46, "crown", 10),
	Pickup(48, 56, "crown", 10)
]

# här körs spelet
while True:
	clear()
	print_map(player, terrain, pickup)
	var = getch() # vänta på att en knapp trycks
	if var == b"w": # upp
		player.move( 0, -1, terrain, pickup) 
	elif var == b"s": # ned
		player.move( 0,  1, terrain, pickup) 
	elif var == b"a": # vänster
		player.move(-1,  0, terrain, pickup) 
	elif var == b"d": # höger
		player.move( 1,  0, terrain, pickup)