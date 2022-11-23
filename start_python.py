'''
Tertius Erskine
November 1st, 2018
'''
def error_percent(actual, guess):
    '''
    error_percent(number, number) --> float
    Returns the percentage error between the actual value and the guessed
    value, as a percentage (i.e. returns 2.4 for 2.4%, not 0.024).
    '''    
    diff = actual - guess
    if diff < 0:
        diff *= -1
    return diff / actual * 100


def xor(bool1, bool2):
    '''
    xor(bool, bool) --> bool
    Returns an exclusive-or value, which evaluates to True only when one of the
    two inputs is True but not both (i.e. returns False for True and True, not True).
    '''
    if bool1 == bool2:
        return False
    else:
        return True
   
   
def print_truths(bool1,bool2):
    '''
    print_truths(bool, bool) --> None
    Takes two boolean values and prints their results for each boolean
    operator including xor (exclusive-or), nor (not-or) and nand (not-and).
    '''
    or1 = bool1 or bool2
    and1 = bool1 and bool2
    xor1 = xor(bool1,bool2)
    
    print("{} OR {} = {}".format(bool1,bool2,or1))
    print("{} AND {} = {}".format(bool1,bool2,and1))
    print("{} XOR {} = {}".format(bool1,bool2,xor1))
    print("{} NOR {} = {}".format(bool1,bool2,not(or1)))
    print("{} NAND {} = {}".format(bool1,bool2,not(and1)))
    

def tiles_needed(width, length, t_dimension):
    '''
    tiles_needed(int, int, int) --> int
    Takes 3 integer values representing width, length and tile size returning an integer
    representing the number of square tiles needed to properly cover the area of a given rectangle.
    '''
    dimension1 = (width//t_dimension)
    dimension1r = (width%t_dimension)
    dimension2 = (length//t_dimension)
    dimension2r = (length%t_dimension)
    if dimension1r != 0:
        dimension1 = (dimension1 + 1)
    if dimension2r != 0:
        dimension2 = dimension2 +1
    return dimension1 * dimension2


def is_right_triangle(len1, len2, len3):
    '''
    is_right_triangle(number, number, number) --> bool
    Takes the value of three numbers (could be integers or floats) and returns a boolean value (True 
    or False) based on whether or not the three numbers (given in any order) can form a right triangle.
    '''
    if len1 > len2 and len1 > len3:
        hypotenuse = len1**2
        base_height = (len2**2 + len3**2)
    elif len2 > len1 and len2 > len3:
        hypotenuse = len2**2
        base_height = (len1**2 + len3**2)
    else:
        hypotenuse = len3**2
        base_height = (len1**2 + len2**2)
        
    if base_height == hypotenuse or error_percent(hypotenuse, base_height) <= 1.0 :
        return True
    else:
        return False


def convert_mins(mins, unit):
    '''
    convert_mins(int, str) --> float
    Takes an integer value representing minutes and a string representing a chosen unit of time
    returning a float representing the given number of minutes converted to the desired unit given.
    '''
    s = mins*60
    h = mins/60
    d = h/24
    y = d/365
    
    if unit == "s": 
        return '{}'.format(float(s))
    elif unit == "h": 
        return '{}'.format(float(h))
    elif unit == "d": 
        return '{}'.format(float(d))
    elif unit == 'y':
        return '{}'.format(float(y))
    else:
        return '{}'.format(float(mins))

 
def clock_string(int1):
    '''
    clock_string(int) --> str
    Takes an integer representing a number of minutes and returns a string representing
    the given number of minutes (or the integer) as days, hours, and minutes.
    '''
    if int1 < -1440:
        return '-{}d:{:0>2}h:{:0>2}m'.format(int1//-1440,(int1%-1440)//-60,((int1%-1440)%-60)*-1)
    elif int1 > -1440 and int1 < 0:
        return '-{:0>2}h:{:0>2}m'.format(int1//-60,(int1%-60)*-1)
    elif int1 >=0 and int1 <1440:
        return '{:0>2}h:{:0>2}m'.format(int1//60,int1%60)
    else:
        return '{}d:{:0>2}h:{:0>2}m'.format(int1//1440,(int1%1440)//60,(int1%1440)%60)


def rock_paper_scissors(p1, p2):
    '''
    rock_paper_scissors(str, str) --> int
    Takes two strings representing rock, paper or scissors and returns an integer 
    representing the winner (1 for Player1, 2 for Player 2 and 0 for a draw).
    '''
    if ((p1 =='r' or p1 =='R') and (p2 =='r' or p2 =='R')) or ((p1 =='s' or p1 =='S') and (p2 =='s' or p2 =='S')) or ((p1 =='p' or p1 =='P') and (p2 =='p' or p2 =='P')):
        return 0
    if (p1 =='r' or p1 =='R') and (p2 =='p' or p2 =='P'):
        return 2
    elif (p1 =='p' or p1 =='P') and (p2 =='s' or p2 =='S'):
        return 2
    elif (p1 =='s' or p1 =='S') and (p2 =='r' or p2 =='R'):
        return 2
    else:
        return 1
    
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    
    print("CHOOSE YOUR OPTION:")
    print("1. Logical Functions")
    print("2. Geometry Functions")
    print("3. Time Functions")
    print("4. Play")
    choice = input("Enter your choice(1/2/3/4): ")
    
    if choice == '1':
        bool1 = input("Enter your first boolean value(T/F): ")
        bool2 = input("Enter your second boolean value(T/F): ")
        if bool1 == 'T':
            bool1 = True
        else:
            bool1 = False
        if bool2 == 'T':
            bool2 = True
        else:
            bool2 = False
        print_truths(bool1, bool2)
        
    elif choice == '2':
        print("CHOOSE YOUR OPTION:")
        print("1. Tile Calculator")
        print("2. Triangle checker")
        choice1 = input("Enter your choice(1/2): ")
        
        if choice1 == '1':
            width = int(input("Width of area: "))
            length = int(input("Length of area: "))
            t_dimension = int(input("Size of square tile: "))
            tiles_needed1 = tiles_needed(width,length, t_dimension)
            
            print("A {}x{} area needs {} {}x{} square tiles.".format(width, length, tiles_needed1, t_dimension, t_dimension))
            
        else:
            len1 = float(input("Side 1 Length: "))
            len2 = float(input("Side 2 Length: "))
            len3 = float(input("Side 3 Length: "))
            
            if is_right_triangle(len1, len2, len3) == True:
                print("A {}-{}-{} triangle IS a right-triangle.".format(len1, len2, len3))
            else:
                print("A {}-{}-{} triangle is NOT a right-triangle.".format(len1, len2, len3))
                
    elif choice == '3':
        mins = int(input("Enter a number of minutes: "))
        unit = input("Enter a unit to convert to (y=years, d=days, h=hours, s=seconds): ")
        print("{} mins = {:.2f}{}".format(mins, float(convert_mins(mins, unit)), unit))
        print("{} mins = {:.2f}".format(mins, clock_string(mins)))
        
    elif choice == '4':
        p1 = input("Player 1 (r/p/s): ")
        p2 = input("Player 2 (r/p/s): ")
        winner = rock_paper_scissors(p1, p2)
        if winner == 0:
            print('Draw!')
        elif winner == 1:
            print('Player 1 wins!')
        else:
            print('Player 2 wins')
            
    else:
        print("INVALID CHOICE")