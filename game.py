import random
random



def get_name():
    global name
    name = input("Make a name for your frend\n> ")
    start()

def start():
    global place
    
    print("You and "+name+" are going Mountain Biking!")
    print("Choose a place to go Mountain Biking! with "+name+".")
    print("1 Lake Rebecca")
    print("2 Elm Creek")
    print("3 Hillside Park")

    choice = int(input("> "))
    choice

    try:
        if choice == 1:
            place = ("Lake Rebecca")
            print("You and "+name+" are going to "+place)
            car()
        elif choice == 2:
            place = ("Elm Creek")
            print("You and "+name+" are going to "+place)
            car()
        elif choice == 3:
            place = ("Hillside Park")
            print("You and "+name+" are going to "+place)
            car()
        else:
            print("You did not give me the right number")
            start2()
    except:
        print("You did not give me a number TRY AGEN")
        start2()

def start2():
    print("1 Lake Rebecca")
    print("2 Elm Creek")
    print("3 Hillside Park")

    choice = int(input("> "))
    choice

    try:
        if choice == 1:
            place = ("Lake Rebecca")
            print("You and "+name+" are going to "+place)
            car()
        elif choice == 2:
            place = ("Elm Creek")
            print("You and "+name+" are going to "+place)
            car()
        elif choice == 3:
            place = ("Hillside Park")
            print("You and "+name+" are going to "+place)
            car()
        else:
            print("You did not give me the right number")
            start2()
    except:
        print("You did not give me a number TRY AGEN")
        start2()

def car():
    try:
        print("Now you and "+name+" go to the Garage")
        print("You and "+name+" have to pick a car here are your choices")
        print("1 Subaru Outback (very reliable 1 out of 20 chance for a break down)")
        print("2 Honda Civic (kind of reliable 1 out of 10 chance for a break down)")
        print("3 Lamborghini Huracan (not vary reliable 1 out of 5 chance for break down)")
        
        choice = int(input("> "))
        choice

        if choice == 1:
            print("you and "+name+" picked the very reliable Subaru Outback")

            rate = random.randint(1,20)
            if rate == 1:
                print("Your Subaru Outback broke down")
                deth1()
            else:
                print("The Subaru Outback made it")
                trail()

        elif choice == 2:
            print("you and "+name+" picked the kind of reliable Honda Civic")

            rate2 = random.randint(1,10)
            if rate2 == 1:
                print("Your Honda Civic broke down")
                deth1()
            else:
                print("the Honda Civic made it")
                trail()

        elif choice == 3:
            print("you and "+name+" picked the not vary reliable Lamborghini Huracan")

            rate3 = random.randint(1,5)
            if rate3 == 1:
                print("Your Lamborghini Huracan broke down")
                deth1()
            else:
                print("Your Lamborghini made it")
                trail()

    except:
        print("You did not give me a number TRY AGEN")
        car2()

def car2():
    try:
        print("1 Subaru Outback (very reliable)")
        print("2 Honda Civic (kind of reliable)")
        print("3 Lamborghini Huracan (not vary reliable)")
    
        choice = int(input("> "))
        choice
    
        if choice == 1:
            print("you and "+name+" picked the very reliable Subaru Outback")
        
            rate = random.randint(1,20)
            if rate == 1:
                print("Your Subaru Outback broke down")
                deth1()
            else:
                print("The Subaru Outback made it")
                trail()
                
        elif choice == 2:
            print("you and "+name+" picked the kind of reliable Honda Civic")
        
            rate2 = random.randint(1,10)
            if rate2 == 1:
                print("Your Honda Civic broke down")
                deth1()
            else:
                print("the Honda Civic made it")
                trail()
        
        elif choice == 3:
            print("you and "+name+" picked the not very reliable Lamborghini Huracan")
        
            rate3 = random.randint(1,5)
            if rate3 == 1:
                print("Your Lamborghini Huracan broke down")
                deth1()
            else:
                    print("Your Lamborghini made it")
                    trail()

    except:
        print("You did not give me a number TRY AGEN")
        car2()

def deth1():
    try:
        print("deth 1 You died to a bear after your car broke down and you climbed the mountain to look for help. The bear ate you and "+name+" alive.")
        print("1 play again")
        print("2 dont play again")

        choice = int(input("> "))

        if choice == 1:
            print("Ok playing again")
            get_name()

        elif choice == 2:
            print("Ok ending the game")
        else:
            deth12()

    except:
        print ("You did not give me a number")
        deth12()

def deth12():
    try:
        print("deth 1 You died to a bear after your car broke down and you climbed the mountain to look for help. The bear ate you and "+name+" alive.")
        print("1 play again")
        print("2 dont play again")
        
        choice = int(input("> "))
        
        if choice == 1:
            print("Ok playing again")
            get_name()
        elif choice == 2:
            print("Ok ending the game")

    except:
        print ("You did not give me a number")
        deth1_2()

def trail():
    try:
        print("Now you and "+name+" at "+place+" and thare are 5 Trails")
        print("1 candy Trail")
        print("2 normal Trail")
        print("3 code Trail")
        print("4 mushroom Trail")

        choice = int(input("> "))

        if choice == 1:
            candy_trailstart()
        elif choice == 2:
            normal_trailstart()
        elif choice == 3:
            code_trailstart()
        elif choice == 4:
            mushroom_trailstart()
        else:
            print("Not a number")
            trail1()
    except:
        print("Not a number")
        trail1()

def trail1():
        try:
            print("1 candy Trail")
            print("2 normal Trail")
            print("3 code Trail")
            print("4 mushroom Trail")
    
            choice = int(input("> "))
    
            if choice == 1:
                candy_trailstart()
            elif choice == 2:
                normal_trailstart()
            elif choice == 3:
                code_trailstart()
            elif choice == 4:
                mushroom_trailstart()
            else:
                print("Not a number")
                trail1()
        except:
            print("Not a number")
            trail1()

def candy_trailstart():
    try:
        print("You and "+name+" picked the Candy Trails")
        print("1 go and do the Candy Trails")
        print("2 go back")
    
        choice = int(input("> "))

        if choice == 1:
            print("Ok now doing the Candy Trails")
            print("deth 2 you and "+name+" go and try to do the Candy trail but you and "+name+" get lost half way and find some barrys you eat them and\n die but "+name+" survives for 2 more days before dying")
            dethcandy1
        elif choice == 2:
            trail1()
        else:
            print("you did not give me the right number")
            candy_trailstart2()
    except:
        print("you did not give me a number")
        candy_trailstart2

def candy_trailstart2():
    try:
        print("You and "+name+" picked the Candy Trails")
        print("1 go and do the Candy Trails")
        print("2 go back")
    
        choice = int(input("> "))

        if choice == 1:
            print("Ok now doing the Candy Trails")
            print("deth 2 you and "+name+" go and try to do the Candy trail but you and "+name+" get lost half way and find some barrys you eat them and\n die but "+name+" survives for 2 more days before dying")
            dethcandy1()
        elif choice == 2:
            trail1()
        else:
            print("you did not give me the right number")
            candy_trailstart2()
    except:
        print("you did not give me a number")
        candy_trailstart2()

def dethcandy1():
    try:
        print("1 play again")
        print("2 dont play again")
        
        choice = int(input("> "))
        
        if choice == 1:
            print("Ok playing again")
            get_name()
        elif choice == 2:
            print("Ok ending the game")
        else:
            print("You did not give me the right number")
            dethcandy12()

    except:
        print ("You did not give me a number")  
        dethcandy12()

def dethcandy12():
    try:
        print("1 play again")
        print("2 dont play again")
        
        choice = int(input("> "))
        
        if choice == 1:
            print("Ok playing again")
            get_name()
        elif choice == 2:
            print("Ok ending the game")
        else:
            print("You did not give me the right number")
            dethcandy12()

    except:
        print ("You did not give me a number") 

def normal_trailstart():
    try:
        
        print ("You and "+name+" picked the boring normal Trail")
        print("1 do the normal Trail")
        print("2 go back")

        choice = int(input("> "))

        if choice == 1:
            print("going on the Boring Normal Trail")
            normal_trailtrail()
        elif choice == 2:
            trail1()
        else:
            print("did not give me the right number")
            normal_trailstart1()

    except:
        print("did not give me a number")
        normal_trailstart1()

def normal_trailstart1():
    try:

        print("1 do the normal Trail")
        print("2 go back")
        
        choice = int(input("> "))
        
        if choice == 1:
            print("going on the Boring Normal Trail")
            normal_trailtrail()
        elif choice == 2:
            trail1()
        else:
            print("did not give me the right number")
            normal_trailstart1()
    except:
        print("did not give me a number")
        normal_trailstart1()

def normal_trailtrail():
    try:

        print("YOU AND "+name+" ARE GOING DOWN THE NORMAL TRAIL ")
        print("THERE IS A JUMP COMING UP  ")
        print("1 HIT THE JUMP")
        print("2 DONT HIT JUMP")

        choice = int(input("> "))

        if choice == 1:
            print("You and "+name+" hit the jump but you hit your head all you remember is hiting the jump and ending up in your bed in the morning")
        elif choice == 2:
            print("You and "+name+" dont hit the jump you try to go arownd but thare is a hole you both fall in deth 3")
            dethnormal()
        else:
            print("you did not give me the right number")
            normal_trailtrail1()

    except:
        print("did not give me a number")
        normal_trailtrail1

def normal_trailtrail1():
    try:

        print("YOU AND "+name+" ARE GOING DOWN THE NORMAL TRAIL ")
        print("THERE IS A JUMP COMING UP  ")
        print("1 HIT THE JUMP")
        print("2 DONT HIT JUMP")

        choice = int(input("> "))

        if choice == 1:
            print("You and "+name+" hit the jump but you hit your head all you remember is hiting the jump and ending up in your bed in the morning")
        elif choice == 2:
            print("You and "+name+" dont hit the jump you try to go arownd but thare is a hole you both fall in deth 3")
            dethnormal()
        else:
            print("you did not give me the right number")
            normal_trailtrail1()

    except:
        print("did not give me a number")
        normal_trailstart1

def srvive():
    try:

        print("1 play again")
        print("2 dont play again")

        choice = int(input("> "))
        if choice == 1:
            print("Ok playing again")
            get_name()
        elif choice == 2:
            print("Ok ending the game")
        else:
            print("You did not give me the right number")
            srvive()

    except:
        print("You did not give me the right number")
        srvive()


def dethnormal():
    try:
        print("1 play again")
        print("2 dont play again")
        
        choice = int(input("> "))
        
        if choice == 1:
            print("Ok playing again")
            get_name()
        elif choice == 2:
            print("Ok ending the game")
        else:
            print("You did not give me the right number")
            dethnormal1()

    except:
        print ("You did not give me a number")  
        dethnormal1()

def dethnormal1():
    try:
        print("1 play again")
        print("2 dont play again")
        
        choice = int(input("> "))
        
        if choice == 1:
            print("Ok playing again")
            get_name()
        elif choice == 2:
            print("Ok ending the game")
        else:
            print("You did not give me the right number")
            dethnormal1()

    except:
        print ("You did not give me a number")  
        dethnormal1()




get_name()