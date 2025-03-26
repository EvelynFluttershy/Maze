from classes import *
from functions import *
clear () # för att tomma skärmen varja gång innan kör programmet.
print(" name your character:")
var= input()
player = Player(50,50,var)
terrain = [
   Terrain(45,51,"tree"),
   Terrain(47,52,"tree"),
   Terrain(48,44,"tree"),
   Terrain(49,55,"tree"),
   Terrain(53,46,"tree"),
]
pickup=[
  Pickup(52,46,"crown",10),
  Pickup(48,56,"crown",10)


]

# kör spelet
while True :
    clear()
    print_map(player,terrain,pickup)
    var = getch()#likna input 
    if var == b"w":
      player.move(0,-1,terrain,pickup) 
    elif var == b"s":
      player.move(0,1,terrain,pickup) 
    elif var == b"a":
      player.move(-1,0,terrain,pickup) 
    elif var == b"d":
      player.move(1,0,terrain,pickup)
 #     

