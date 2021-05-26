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
print(''' -------------------------------------------
                 SCORE
-------------------------------------------''')
n = 1
for element in score:
    print("Student_" + str(n) + " : " + str(element) + '''/100''')
    n = n+1
    