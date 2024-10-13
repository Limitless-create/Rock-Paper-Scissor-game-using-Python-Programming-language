# STONE,PAPER,SCISSOR GAME 
  
  
import random 
computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")   
youDict={"x":1,"p":-1,"s":0}      
reverseDict={1:"Scissor",-1:"Paper",0:"Stone"}
you=youDict[youstr]  
print(f"your choice:{reverseDict[you]}\ncomputer choice:{reverseDict[computer]}")

if(computer==you):
    print("Neither side gains ground;it's a stalemate!")   
    
else:
    if(computer==-1 and you ==1):
         print("Yaah!You win.Yours scissor slice through,carving out their victory.")
    elif(computer==-1 and you==0):
        print("sorry!You lose.Computer's paper rises to the challenge,folding its way to victory!.") 
    elif(computer==1 and you ==-1):
        print("Oh no!You lose.Computer's scissor prevail,cutting a path to victory!.")
    elif(computer==1 and you==0):
        print("Hurrah!You win.Yours stone triumps,smashing through all obstacles!.")    
    elif(computer==0 and you ==-1):
        print("Woohoo!you win.yours paper covers stone,sealing its triumph!")
    elif(computer==0 and you==1):
        print("Oops!you lose.Computer's stone stands unshaken,crushing all in its path!")    
    else:
        print("something went wrong")            
   
