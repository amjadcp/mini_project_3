'''
Author : Amjad
Date   : 3 JUN 2021 11.30 PM
About  : Hang man game using PYTHON
'''

#IMPORTED PYTHON LIBRARIES
import random
import os
import time
from word_list import fruits, currencies, countries, states
#from colorama import fore  -> cn't download in my computer

'''FUNCTIONS g_m TO g_p FOR HANG MAN'''
def g_m(i):
    if i==2:
        g_2()
    elif i==3:
        g_3()
    elif i==4:
        g_4()
    else:
       None

    

def g_1():
    print(f'''--------------
|            |            
|            o
|
|
|
|
|
|''')

def g_2():
     print(f'''--------------
|            |            
|            0
|           
|            
|           
|
|
|''')

def g_3():
     print(f'''--------------
|            |            
|            0
|           /|\\
|            
|           
|
|
|''')

def g_4():
     print(f'''--------------
|            |            
|            0
|           /|\\
|            |
|           / \\
|
|
|''')

def g_p():
     print(f'''--------------
|            |            
|            o
|           
|            
|            0
|           /|\\
|            |
|           / \\''')





#A FUNCTION TO PRINT HEADING WITH SHOWING ATTEMPT
def head(i, topic):
    print(f'''
    
    ----------------{topic}----------------------------
    
                    
                ✮｡  🎀  𝐻𝒜𝒩𝒢 𝑀𝒜𝒩  🎀  ｡✮

--------------- ATTEMPT = {i} of 4-----------------\n\n''')

# a function to check the answer
def answer(word, limit):
    i = 0
    tem = []
    temp = ""
    Guess = input("Guess the word : ")
    os.system("cls")
    guess = Guess.upper()
    for char in guess:
        if char in word:
            tem.insert(i, char)
        else:
            tem.insert(i, "_")
        i = i+1
    
    return temp.join(tem)
    
def menu():
    topic = ''
    fruits=[
              "Abiu",
              "Açaí",
              "Acerola",
              "Ackee",
              "Africancucumber",
              "Apricot",
              "Avocado",
              "Banana",
              "Bilberry",
              "Blackberry",
              "Blackcurrant",
              "Blacksapote",
              "Blueberry",
              "Boysenberry",
              "Breadfruit"
           ]

    countries=[
              
              "afghanistan",
              "albania",
              "Argentina",
              "america",
              "brazil",
              "Australia",
              "india",
              "pakistan",
              "chaina"
              ]

    currencies = [
        
                    "afghani",
                    "euro",
                    "colon",
                    "crown",
                    "rupee",
                    "doller",
                    "dalasi",
                    "dinar",
                    "kina",
                    "kuna"
                 ]

    states =[
    
                  "bihar",
                  "kerala",
                  "karnadaka",
                  "thamizhndu",
                  "manipur",
                  "mizoram"
              ]   

    print(f'''-------------HANGER MAN TOPIC MENU-------------
              1. ABOUT FRUITS
              2. ABOUT COUNTRIES
              3. ABOUT CURRENCIES
              4. ABOUT STATES''')
    name = input("Good name please : ")
    op = input("Option :")
    if op==1:
       Word = random.choice(fruits)
       topic = 'Guess the fruit'
    elif op==2:
       Word =random.choice(countries)
       topic = "Guess the country"
    elif op==3:
       Word = random.choice(currencies)
       topic = "Guess the currency"
    else:
       Word = random.choice(states)
       topic = "Guess the state"
    print(f'''Hi, {name.upper()} best of luck !''')
    time.sleep(1)
    os.system("cls")  # in ubundu cls -> clear
    return Word, topic






Word, topic = menu()
head(1, topic) #FIRST TIME HEAD CALLING
g_1()    #g_1 CALLING
word = Word.upper()            # UPPER CASE CONVERTION
limit = len(word)
print("\n\n", " _ " * limit, "\n\n")
i = 1
result = False

''' WHILE LOOP THAT REPEATE 4 TIMES '''
while 4>i:
    if i-1 != 0:
      head(i, topic)
    i = i+1
    temp = answer(word, limit)
    ans = ''
    
    for ch in temp:
      ans = ans + ch + ' '
   
    temp_size = len(temp)
    
    if limit<temp_size:
        g_m(i)
        if i>3:
          print("\n NIRTHI VERENTHELUM PANIKKE PODO \n")    #PRINT WHEN FAILE
        else:
         print(f"""Breaked limit (only {limit} letters needed""")

    elif limit>temp_size:
        g_m(i)
        if i>3:
          print("\n NIRTHI VERENTHELUM PANIKKE PODO \n")
        else:
          print(f"""\n\n{limit} letters needed""")

    elif word==temp:         # WORKS WHEN THE GUESSED WORD IS CORRECT
        g_p()
        if i>3:
          print("\n NIRTHI VERENTHELUM PANIKKE PODO \n")
        else:
          result = True
          print('\n', ans, '\n')
          print("\nYOU ARE MY LIFE SAVER\n")
        
    elif limit==temp_size:
         g_m(i)
         if i>3:
           print("\n NIRTHI VERENTHELUM PANIKKE PODO \n")
         else:  
           print('\n', ans, "\n")
           print(f'''\nKEEP GOING\n''')
    else:
        g_m(i)
        if i>3:
            print("\nNIRTTHI VERAVALLA PANIKKUM PODO\n")
        else:
           print(f'''\nKEEP GOING       {limit} letters needed\n''')
        

    if result==True:
      break           # BREAKING THE WHILE LOOP WHEN GET CORRECT ANSWER
   
    print(f"""HINT : {limit} letters needed""")
    op = input("CONTINUE : (y/N)" )
    if op.upper()=='Y':
      os.system("cls")   # in ubundu cls -> clear
      print(f"""HINT : {limit} letters needed""")

    else:
        break

    if i>3:
        print("\n\n THINK \n\n")


    

    

