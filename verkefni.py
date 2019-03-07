################################################
### http://tinyurl.com/forritunarklubbur2019 ###
################################################

def verk1():
    print("Hello")

def verk2():
    print("Hvað heitir þú?")
    nafn = input()
    print("Halló " + nafn)
    
def verkNytt3():
    print("Skrifaðu inn tölu:")
    tala = int(input())
    #print(tala)

    if(tala < 10):
        print("i am small")
    elif(tala > 1000):
        print("vá þetta er risastór tala!!!!!")
    if(10 < tala < 1000):
        print("inside if statement")


def verk3():
    print("gefðu mér tölu:")
    tala = int(input())
    if(tala > 999):
        print("vá þetta er risastór tala")
    elif(tala > 9):
        print("vá þetta er stór tala")
    else:
        print("vá hvað þetta er lítil tala")

def verk4():
    print("ég mun prenta út stærri töluna")
    print("gefðu mér tölu:")
    tala1 = int(input())
    print("gefðu mér aðra tölu:")
    tala2 = int(input())
    if(tala1 > tala2):
        print(str(tala1) + " er stærri en " + str(tala2))
    elif(tala2 > tala1):
        print(str(tala2) + " er stærri en " + str(tala1))
    else:
        print("tölurnar eru jafn stórar")

def verk5():
    print("gefðu mér tölu:")
    tala = int(input())
    #print("Hello world\n" * tala)
    for i in range(tala):
        print("Hello world")


def verk6():
    n = int(input())
    while(True):
        print(n)
        n = n - 1
        if(n == -1):
            break

def verk6odruvisi():
    n = int(input())
    while(n >= 0):
        print(n)
        n = n - 1

def verk6tridjaleid():
    n = int(input())
    for i in range(n, -1, -1):
        print(i)

def verk7():
    n = int(input())

    '''for i in range(0, n):
        for j in range(0, i + 1
                       ):
            print("*", end=" ")
        print()'''
    '''for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()'''

    for i in range(0, n):
        for j in range(0, n - i):
            print("*", end=" ")
        print()

def verk8():
    while(True):
        print("Input a positon between 1 and 10: ", end="")
        tala = int(input())
        if(tala > 10):
            print("number to big")
        elif(tala < 1):
            print("number to low")
        else:
            break
    while(True):
        print("l - for moving left")
        print("r - for moving right")
        print("Any other letter for quitting")
        print("Input your choice: ", end="")
        nextInput = input()
        if(nextInput == "r"):
            if(tala < 10):
                tala += 1
        elif(nextInput == 'l'):
            if(tala > 1):
                tala -= 1
        else:
            print("quit")
            break
        print("New position is: " + str(tala))
    

#verk1()
#verk2()
#verkNytt3()
#verk3()
#verk4()
#verk5()
#verk6()
#verk6odruvisi()
#verk6tridjaleid()
#verk7()
verk8()
