# import libraries
import random

# show idea of  game
print("_________________________________________________________ \n\n")
print("""
Welcome everybody!!
      we will game "rock-paper-scissors" 
      idea of game that you choose one of rock-paper-scissors
      then computer will choose ,too
      if your choice == choice of computer  --> it is tie
      if you : rock & computer : scissors
      or if you : scissors & computer : paper
      or if you : paper & computer : rock

      you will win
      otherwise , computer will win
""")
# game
print("\n _________________________________________________________ \n")
while True :
    PL = input("please choose from (rock (r) ,paper(p) ,scissors(s)) : ")  
    if PL != 'r' and PL != 's' and PL != 'p' :
        print("you enter uncorrect choice , retry ")    
    else:
        break    
print(f"your choice : {PL}")

PC = random.choice(["r","s","p"])
print(f"computer's choice : {PC}")

if PC == PL :
    print("It's tie")
elif PL == 'r' and PC == 's' :
    print("you won")
elif PL == 's' and PC == 'p' :
    print("you won")
elif PL == 'p' and PC == 'r' :
    print("you won")
else :
    print("you lost")            


print("\n\n _________________________________________________________")