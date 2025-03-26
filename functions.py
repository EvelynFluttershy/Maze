import os #för systym functionar
import msvcrt # ett micarosoft functionar
def clear():# toma terminal från texten
    os.system("cls")
def getch():#hämtar knapar från tangbordet
    return msvcrt.getch ()
def xy(array,x,y,value):# vänder på x/y för inmatning till array
    array[y][x] = value
def text_left_right (width,left,right):
    left_len = len(left)
    right_len = len(right)
    spacing = width-left_len-right_len
    return left+" "*spacing+right
       
W=9
C=4

#skapa funkionar för att rita ut spelplan
def print_map(player,terrain,pickup):
    x=player.get_x () 
    y=player.get_y () 
    map=[  
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  "]
     ] 
    
    for t in terrain:
        tx= t.get_x()-x+C#
        ty= t.get_y()-y+C
        if tx>=0 and tx< W and  ty>=0 and ty< W:
          xy(map,tx,ty,t.get_emoji())


    for t in pickup:
        tx= t.get_x()-x+C#
        ty= t.get_y()-y+C
        if tx>=0 and tx< W and  ty>=0 and ty< W:
          xy(map,tx,ty,t.get_emoji())





    map[C][C]= "🔴"

    print(text_left_right(22,player.get_name().upper(),str(player.get_health())+"/"+str(player.get_max_health())))
    print("█"*(W*2+4))
    for i in range (W):
        print("██"+"".join(map[i])+"██")
    print("█"*(W*2+4))
    print(text_left_right(22,f"LEVEL {player.get_level()}",f"{player.get_gold()} G"))
 
    

   