import random
import time
import layout
import pyttsx3
import speech_recognition as sr
import datetime

r = 1
flag = 0
mob = 0
sat = 0
temp = 0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak(f"Good Morning Sir!My name is HAZEL ")

    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon Sir!My name is HAZEL ")

    else:
        speak(f"Good Evening Sir!My name is HAZEL ")


def FiLayout(flag):

    if(flag == 1):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                    0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  | 0                   |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 1,PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")


            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")

            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                flag += 1
                FiLayout(flag)



    elif(flag == 2):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |  0                  |     |\/|      |                     |   | |")
        print(" | |  |  0                  |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 1,PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                flag += 1
                FiLayout(flag)



    elif(flag == 3):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |                    0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  | 0               0   |     |\/|      |                     |   | |")
        print(" | |  | 0                   |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 1,PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                flag += 1
                FiLayout(flag)




    elif(flag == 4):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |                        |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |  0            0     |     |\/|      |                     |   | |")
        print(" | |  |  0            0     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("CONGRATULATIONS!!")
        speak("CONGRATULATIONS PLAYER ONE ! YOU ARE SO LUCKY AND YOU WON THE GAME")

        flag += 1
        FiLayout(flag)

    else:
        print("YOU ALREADY WON THE GAME.")
        exit()







def SeLayout(sat):
    if(sat == 1):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |        0      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |                     0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 2,PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")


            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")

            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                sat += 1
                SeLayout(sat)


    elif(sat == 2):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |        0      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |        0      |                         | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 2, PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                sat += 1
                SeLayout(sat)


    elif(sat == 3):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                      | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |    0   0      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |        0      |                         | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 2, PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                sat += 1
                SeLayout(sat)



    elif(sat == 4):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |                         | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |    0   0      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |    0   0      |                         | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("CONGRATULATIONS!!")
        speak("CONGRATULATIONS PLAYER TWO ! YOU ARE SO LUCKY AND YOU WON THE GAME")
        sat += 1
        SeLayout(sat)

    else:
        print("YOU ALREADY WON THE GAME.")
        exit()


def ThLayout(temp):
    if(temp == 1):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0                    |               |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     0         |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 3, PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")


            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")

            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                temp += 1
                ThLayout(temp)


    elif(temp == 2):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |                        |     0         |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     0         |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |  0                0    |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 3, PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                temp += 1
                ThLayout(temp)


    elif(temp == 3):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |                        |     0         |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     0  0      |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |  0                     |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 3, PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                temp += 1
                ThLayout(temp)



    elif(temp == 4):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                     |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |                        |     0   0     |  0                  0   | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     0   0     |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |                        |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("CONGRATULATIONS!!")
        speak("CONGRATULATIONS PLAYER THREE ! YOU ARE SO LUCKY AND YOU WON THE GAME")
        temp += 1
        ThLayout(temp)

    else:
        print("YOU ALREADY WON THE GAME.")
        exit()






def FoLayout(mob):
    if(mob == 1):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|                   0 |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |  0                      | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 4, PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")


            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")

            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")

            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                mob += 1
                FoLayout(mob)


    elif(mob == 2):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                     |   | |")
        print(" | |  |                     |_____|/\|______|  0               0  |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                  0   | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 4,PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                mob += 1
                FoLayout(mob)


    elif(mob == 3):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |  0                 0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |                  0  |   | |")
        print(" | |  |                     |_____|/\|______|  0               0  |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |  0                      | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("PLAYER 4, PLEASE ROLL DICE ONE MORE TIME YOU GOT 6.")
        b = input("PRESS Y TO ROLL THE DICE: ").upper()
        if (b == 'Y'):
            n_1 = random.randint(1,6)
            if (n_1 == 1):
                print("\033[1;31;40m\n")
                print("----------")
                print("|        |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("----------")



            elif (n_1 ==2):
                print("\033[1;32;40m")
                print("----------")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("|   0    |")
                print("|        |")
                print("----------")

            elif (n_1 == 3):
                print("\033[1;33;40m")
                print("----------")
                print("|   0    |")
                print("|        |")
                print("|        |")
                print("|        |")
                print("|0      0|")
                print("----------")


            elif(n_1 == 4):
                print("\033[1;34;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|       |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif (n_1 == 5):
                print("\033[1;35;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("|   0   |")
                print("|       |")
                print("| 0   0 |")
                print("---------")


            elif(n_1 == 6):
                print("\033[1;36;40m")
                print("---------")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("|       |")
                print("| 0   0 |")
                print("---------")
                mob += 1
                FoLayout(mob)



    elif(mob == 4):
        print(" ------------------------------------------------------------------------")
        print(" | -------------------------------------------------------------------- |")
        print(" | | 0                  0   |               |  0                  0   | |")
        print(" | |                        |    __ __      |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | | 0                  0   |               |  0                  0   | |")
        print("\033[1;34;40m")
        print(" | |------------------------/---------------\-------------------------| |")
        print(" | |                        |_____|  |______|                         | |")
        print(" | |  |                     |     |\/|      |  0               0  |   | |")
        print(" | |  |                     |_____|/\|______|  0               0  |   | |")
        print(" | |                        |     |  |      |                         | |")
        print(" | |------------------------\---------------/-------------------------| |")
        print("\033[1;32;40m")
        print(" | |   0             0      |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |               |                         | |")
        print(" | |                        |     __ __     |                         | |")
        print(" | |   0             0      |               |                         | |")
        print(" | -------------------------------------------------------------------- |")
        print(" ------------------------------------------------------------------------")

        print("\033[1;35;40m")
        print("CONGRATULATION!!")
        speak("CONGRATULATIONS PLAYER FOUR ! YOU ARE SO LUCKY AND YOU WON THE GAME")
        mob += 1
        FoLayout(mob)

    else:
        print("YOU ALREADY WON THE GAME.")
        exit()


time.sleep(1)
wishMe()
speak("WELCOME TO LUDO GAME...")
time.sleep(1)
print("INSTRUCTIONS OF THIS GAME: -")
speak("INSTRUCTIONS OF THIS GAME: -")

print("\033[1;35;40m")
print("IT'S A LUCK GAME SO ANYONE OF THE PLAYER AMONG ALL 4\n")
print("WHOSE ALL MARBELS OUTSIDE THE HOME WILL WIN")
speak("IT'S A LUCK GAME SO ANYONE OF THE PLAYER AMONG ALL FOUR, WHOSE ALL MARBELS OUTSIDE THE HOME WILL WIN THE GAME. ")
time.sleep(2)
print("\033[1;35;40m")
if __name__ == "__main__":

    while True:
        speak("LET'S START THE LUDO GAME")
        time.sleep(1)
        S = input("TYPE START TO START THE GAME: ").lower()
        while True:
            if(S == 'start'):
                print("\033[1;35;40m")
                a = input("PLAYER 1, PRESS Y TO ROLL THE DICE: ").upper()
                if (a == 'Y'):
                    if(r == 1):
                        n = random.randint(1,6)
                        if (n == 1):
                            print("\033[1;31;40m\n")
                            print("----------")
                            print("|        |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("----------")


                        elif (n ==2):
                            print("\033[1;32;40m")
                            print("----------")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("----------")
                        elif (n == 3):
                            print("\033[1;33;40m")
                            print("----------")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("|        |")
                            print("|0      0|")
                            print("----------")

                        elif(n == 4):
                            print("\033[1;34;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|       |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif (n == 5):
                            print("\033[1;35;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|   0   |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif(n==6):
                            print("\033[1;36;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")
                            print("\n")
                            flag += 1
                            FiLayout(flag)
                print("\033[1;35;40m")
                a = input("PLAYER 2, PRESS Y TO ROLL THE DICE: ").upper()
                if(a == 'Y'):
                    if(r == 1):
                        n = random.randint(1,6)
                        if (n == 1):
                            print("\033[1;31;40m\n")
                            print("----------")
                            print("|        |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("----------")


                        elif (n ==2):
                            print("\033[1;32;40m")
                            print("----------")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("----------")
                        elif (n == 3):
                            print("\033[1;33;40m")
                            print("----------")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("|        |")
                            print("|0      0|")
                            print("----------")

                        elif(n == 4):
                            print("\033[1;34;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|       |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif (n == 5):
                            print("\033[1;35;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|   0   |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif(n==6):
                            print("\033[1;36;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")
                            print("\n")
                            sat += 1
                            SeLayout(sat)


                print("\033[1;35;40m")
                a = input("PLAYER 3, PRESS Y TO ROLL THE DICE: ").upper()
                if(a == 'Y'):
                    if(r == 1):
                        n = random.randint(1,6)
                        if (n == 1):
                            print("\033[1;31;40m\n")
                            print("----------")
                            print("|        |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("----------")


                        elif (n ==2):
                            print("\033[1;32;40m")
                            print("----------")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("----------")
                        elif (n == 3):
                            print("\033[1;33;40m")
                            print("----------")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("|        |")
                            print("|0      0|")
                            print("----------")

                        elif(n == 4):
                            print("\033[1;34;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|       |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif (n == 5):
                            print("\033[1;35;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|   0   |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif(n==6):
                            print("\033[1;36;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")
                            print("\n")
                            temp += 1
                            ThLayout(temp)


                print("\033[1;35;40m")
                a = input("PLAYER 4, PRESS Y TO ROLL THE DICE: ").upper()
                if (a == 'Y'):
                    if(r == 1):
                        n = random.randint(1,6)
                        if (n == 1):
                            print("\033[1;31;40m\n")
                            print("----------")
                            print("|        |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("----------")


                        elif (n ==2):
                            print("\033[1;32;40m")
                            print("----------")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("|   0    |")
                            print("|        |")
                            print("----------")
                        elif (n == 3):
                            print("\033[1;33;40m")
                            print("----------")
                            print("|   0    |")
                            print("|        |")
                            print("|        |")
                            print("|        |")
                            print("|0      0|")
                            print("----------")

                        elif(n == 4):
                            print("\033[1;34;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|       |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif (n == 5):
                            print("\033[1;35;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("|   0   |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")

                        elif(n==6):
                            print("\033[1;36;40m")
                            print("---------")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("|       |")
                            print("| 0   0 |")
                            print("---------")
                            print("\n")
                            mob += 1
                            FoLayout(mob)

                else:
                    print("Exiting game...")
                    time.sleep(2)
                    print("Thanks for playing the game.")
                    speak("Thanks for playing the game.")
                    exit()
