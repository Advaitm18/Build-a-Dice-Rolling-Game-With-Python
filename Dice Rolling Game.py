from random import *     # Built-In Random Module
import dicedisplay       # User-Defined Module

count  = 1
total1 = 0
total2 = 0

name = input("Enter the Username: ")
print(f"Player 2 is Computer")
print("\n----------------------------------")

while (count < 6):
     print((f"+++ Round {count} +++").center(33))
 
     print("\n1. roll the dice          2. exit \n----------------------------------")
     user = int(input("what you want to do??? "))   
     if user==1:
          count += 1      
          roll1 = randint(1,6) #randint [Return a number between 1 and 6 (both inclusive)]
          print(f"\n{name}: ")
          dicedisplay.dice(roll1)
          total1 += roll1

          roll2 = randint(1,6)
          print("\nPlayer 2: ")
          dicedisplay.dice(roll2)
          total2 += roll2 
           
     elif user==2:
          print("You are quitting the game...")
          break

     else:
          print("Wrong Choice")

print("\n\n======== POINT TABLE ========")
print(f"{name}                   {total1}")
print(f"Player2                  {total2}")
print("=============================")
      
if total1 > total2:
     print(f"\nCONGRATULATIONS !!! YOU WON with {total1} points"+"\U0001F603")
elif total1 < total2:
     print(f"\nPLAYER2 WON  with {total2} points..."+"Better Luck Next time! \U0001F605")
else:
     print("\nIt is a tie!"+"\U0001F611")
        
 


