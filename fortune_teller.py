import random
import time
print("Im the Fortune Teller Welcome to my cave I will ask you 3 questons and give you a fortune\n...")
time.sleep(5)
def fortune_questons():
    try:
        queston1 = int(input("What is the month of your birthday\n> "))
        queston1
        try:     
            queston2 = int(input("what is your luckey number\n> "))
            queston2
            try:
                queston3 = int(input("what is the frst number of the year you were born\n> "))
                queston3
                picked_number =(random.randint(1,5))
                if picked_number == 1:
                     print("You fortune is good luck")
                elif picked_number == 2:
                     print("your fortune is poop")
                elif picked_number == 3:
                     print("your fortune is lots of ice creem")
                elif picked_number == 4:
                     print("you have bad luck 3 years")
                else:
                     print("you have the best luck")     
            except:
                print("THAT IS NOT YOUR FRST NUMBER OF THE YEAR YOU WERE BORN")
                fortune_questons()    
        except:
                 print("THAT IS NOT YOURE LUCKEY NUMBER")
                 fortune_questons()
    except:        
        print("THAT IS NOT YOUR BRTHDAY MONTH")
        fortune_questons()
fortune_questons()         