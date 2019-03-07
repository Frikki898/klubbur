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

#verk1()
#verk2()
verkNytt3()
#verk3()
#verk4()
#verk5()
