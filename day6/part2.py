import math
import numpy as np

def main():
    with open("input.txt", mode="r") as inputfile:
   #     with open("example.txt", mode="r") as inputfile:
       problems = []
       for line in inputfile:
           line = line.rstrip("\n")
           problems.append([ch for ch in line])
       problemanswertotal = 0
       print(problems)
       problemlength = len(problems)
       #problemamount = len(problems[0])
       actions = problems.pop()
       #actions.append(' ')
       #ctions.append(' ')
       newproblems = []
       newproblems.append([])
       problempart = 0
       #print(newproblems[0])
       for action in range(0,len(actions)):
 #          print(action)
           if actions[action] != " ":
              newproblems[problempart].append(actions[action])
           numberstring = ""

           for numbers in range(0,len(problems)):
               #numberstring = ""
               numberstring = str(numberstring) + str(problems[numbers][action])
               print("Building string " + numberstring)
           print(numberstring)
           if not numberstring.isspace():
               #newproblems[action].append([])
               print(newproblems[problempart])
 #              print(type(newproblems[problempart]))
               newproblems[problempart].append(numberstring)
           else:
               newproblems.append([])
               problempart = problempart + 1
           print(newproblems)

#       print(newproblems)


       problemamount = len(newproblems)
       for problemnumber in range(0,problemamount):
           problem2 = newproblems[problemnumber]
           problemanswer = 0
    #          for problempart2 in range(0,problemamount):

     #          problem2.append(newproblems[problempart2][problemnumber])
           print(problem2)
           mathaction = problem2.pop(0)
           print(problem2)
           print(mathaction)
           #problem = convertproblem(problem)
           problem2 = [int(x) for x in problem2]
           if mathaction == "*":
               problemanswer = math.prod(problem2)
           elif mathaction == "+":
               problemanswer = sum(problem2)
           print("addin to total: " + str(problemanswer))
           problemanswertotal = problemanswertotal + problemanswer
       print("Total is " + str(problemanswertotal))




if __name__ == '__main__':
    main()
