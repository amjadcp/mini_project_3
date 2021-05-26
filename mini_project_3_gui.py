'''
Author : Amjad
Date   : 26.5.2021
About  : Small program to find score of student
'''
import tkinter

def whole():
    key_file = open("answer_key.txt", "r")
    key = key_file.readlines()
    n = 0
    score = []
    while n<50:
      i = 0
      ans_file = open(f'''answers/student_{n+1}.txt''', "r")
      ans = ans_file.readlines()
      for data in key:
        for element in ans:
          if data==element:
             i = i+1
      n = n+1
      score.append(i)
    save_file = open("whole_score.txt", "a")
    save_file.write(''' -------------------------------------------
                 SCORE
    -------------------------------------------\n''')
    n = 1
    for element in score:
      save_file.write("Student_" + str(n) + " : " + str(element) + '''/100 \n''')
      n = n+1
    save_file.close()
    message = tkinter.Label(window, text="Score of all student on whole_score.txt").grid(row=4)

def student():
    a = Name.get()
    key_file = open("answer_key.txt", "r")
    key = key_file.readlines()
    ans_file = open(f'''answers/{a}''', "r")
    ans = ans_file.readlines()
    i = 0
    for data in key:
      for element in ans:
         if data==element:
             i = i+1
    message = tkinter.Label(window, text=f'''Score of this student : {i}''').grid(row=4)
    


window = tkinter.Tk()
window.title("Score Checker")
window.geometry("600x500")
name = tkinter.Label(window, text="Student file in answers folder:").grid(row=0)
Name = tkinter.Entry(window).grid(row=0, column=1)
null = tkinter.Label(window).grid(row=1)
null = tkinter.Label(window).grid(row=2)
button = tkinter.Button(window, text="Done", command=student).grid(row=3)
button_2 = tkinter.Button(window, text="Score of all students", command=whole).grid(row=3, column=1)
window.mainloop()
