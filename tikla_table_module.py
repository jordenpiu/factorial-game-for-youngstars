import random
def ask():
    choice = int(input("Do you want to play the game?if yes press 1 else 0"))   #take the choice
    return choice
def show_the_num():
    no = random.randrange(1,90)                       #rpint the random no
    print (no)
    return no
def mult():
    print("to get the above shown number as a result of multiplication")
    a =  int (input("enter the first no"))                         #multiply two no
    b = int( input("enter the second no"))
    mult = a*b
    return mult
def compare(n,m):
    if (m == n):
        print("you win!")                                        #declare result
    else:
        print("try once again")



if  __name__ == '__main__':
    x = ask()
    while (x == 1):
        n = show_the_num()
        m = mult()
        compare(n,m)
        ask()
