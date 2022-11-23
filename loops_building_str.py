'''
Tertius Erskine
December 20 2018
Task 2 - Loops and building strings
'''

import random

def sum_string(int1, int2):
    '''
    sum_string(int, int) --> str
    Takes two integer statements representing a range. It builds up a string representing numbers within
    the range and the sum of the numbers then returns the string.(i.e sum_string(1,3) --> 1 + 2 + 3 = 6).
    '''
    print1 = ""
    total = 0
    range1 = range(int1, int2+1)
    
    if int1 > int2:
        range1 = range(int1,int2-1,-1)
    for number in range1:
        if number == int1:
            total += number
            print1 += "{}".format(number)  
        elif number < 0:
            print1 += " + ({})".format(number)
            total += number 
        else:
            total += number
            print1 += " + {}".format(number)  
            
    return "{} = {}".format(print1, total)


def replace(str1,rep_str,rep,occ):
    '''
    replace(str,str,str,int) --> str
    Takes 4 values ,3 strings and one integer then returns a string, it uses the first (a string) as a base.
    It takes the second value representing the character you want to replace in the base. The then what you
    want to replace that character with. Finally, the fourth value represents the occurence of the character 
    in the base in which you want to replace. ) affects all occurences.(i.e. replace('hello','l','a',2)--> 'helao')
    '''
    print1 = ""
    counter = 0
    
    for rep1 in str1:
        if occ == 0 and rep1 == rep_str:
            print1 += "{}".format(rep) 
        elif rep1 == rep_str:
            counter +=1
            if occ == counter:
                print1 += "{}".format(rep) 
            else:
                print1 += "{}".format(rep1)  
        else:
            print1 += "{}".format(rep1)     
            
    return(print1)

def get_to_one(int1):
    '''
    get_to_one(int) --> str
    Takes an integer statement and runs a series of equations on that integer until it is equal to 1.
    It builds up a string of the integer after each equation and returns the string along with the
    largest number within the full series of equations.
    '''
    print1 = ""
    counter = 0
    original = int1
    print1 += "{}\n".format(int1) 
    largest = 0
    
    while int1 != 1:  
        if int1 > largest and int1 >= original:
            largest = int(int1)
        if (int1**0.5)%1 == 0:
            counter += 1
            int1 **= 0.5
            print1 += "{}\n".format(int(int1)) 
        elif int1%2 == 0:
            counter += 1
            int1 //= 2
            print1 += "{}\n".format(int(int1)) 
        else:
            counter += 1
            int1 = (int1 * 3) + 1
            print1 += "{}\n".format(int(int1)) 
            
    return "{}{} got to 1 in {} steps, largest was {}".format(print1,original,counter,largest)


def scraps(int1):
    '''
    scraps(int) --> str
    Takes an integer statement representing the number of rounds you want to play. It then rolls 3
    four sided dice representing your target. After the first stage it rolls 2 six (using random module). 
    sided dice until it is equal to your target. It then builds up a string using your target and the results 
    of rolling the two six sided dice. It then returns the string with its respective points system.
    '''
    total = 0 
    print1 = ""
    rounds = 0
    str_format = "\n[{}] [{}]--> {}"
    
    for stage in range(1,int1 + 1):
        points = 0
        rounds += 1
        target = (random.randrange(1,5) + random.randrange(1,5) + random.randrange(1,5))
        
        if target == 12:
            print1 += "\nROUND #{} --> INSTANT LOSS (-10)!".format(rounds)
            points = points - 10
            total = total - 10
        else:
            print1 += "\nTarget for round {} is {}:".format(rounds, target) 
            dice_sum = 0
            while dice_sum != target:         
                dice1 = (random.randrange(1,7))
                dice2 = (random.randrange(1,7))
                dice_sum = dice1 + dice2
                
                if dice_sum == target:
                    print1 += str_format.format(dice1, dice2, "match")
                    print1 += "\nROUND #{} --> {} POINTS".format(rounds,points)
                elif dice_sum == 2:
                    print1 += str_format.format(dice1, dice2, '-5')
                    points -= 5
                    total -= 5
                elif dice_sum == 12:
                    print1 += str_format.format(dice1, dice2, '+5')
                    points += 5
                    total += 5
                else:
                    print1 += str_format.format(dice1, dice2, '+1')
                    points += 1
                    total += 1
        if rounds == int1:
            print1 += "\nOVERALL: {} POINTS ({:.2f} PER ROUND)".format(total,total/rounds)
             
    return(print1)


#==== INTERACTIVE TESTING CODE =================================================
if __name__ == "__main__":
    
    menu = "Choose a part to test:\n1. sum_string\n2. replace\n3. get_to_one\n4. scraps\n5. Quit\nChoice: "
    choice = input(menu)
    menu = "\n" + menu
    
    while choice != '5': 
        
        if choice == '1':
            int1 = int(input("First number: "))
            int2 = int(input("Second number: "))
            print(sum_string(int1, int2))
            choice = input("{}".format(menu))
        elif choice == '2':
            str1 = input("Enter some string: ")
            rep_str = input("Character to replace: ")
            rep = input("String to replace it with: ")
            occ = int(input("Which occurrence to replace: "))
            print("Result: {}".format(replace(str1, rep_str, rep, occ)))
            choice = input("{}".format(menu))    
        elif choice == '3':
            int1 = int(input("Enter an int to start with: "))
            while int1 < 0:
                int1 = int(input("Enter a positive int to start with: "))
            print(get_to_one(int1))
            choice = input("{}".format(menu))
        elif choice == '4':
            int1 = int(input("How many rounds? (2-8): "))
            while int1 < 2 or int1 > 8:
                int1 = int(input("How many rounds? (2-8): "))
            print(scraps(int1))
            choice = input("{}".format(menu)) 
        else:
            choice = input("\nInvalid choice.{}".format(menu))
        
    print("Goodbye!")