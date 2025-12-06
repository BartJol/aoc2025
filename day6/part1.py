import math

def main():
    with open("input.txt", mode="r") as inputfile:
   # with open("example.txt", mode="r") as inputfile:
       problems = []
       for line in inputfile:
           line = line.rstrip()
           problems.append(line.split())
       problemanswertotal = 0
       #print(problems)
       problemlength = len(problems)
       problemamount = len(problems[0])
       for problemnumber in range(0,problemamount):
           problem = []
           problemanswer = 0
           for problempart in range(0,problemlength):

               problem.append(problems[problempart][problemnumber])
           action = problem.pop()
#           print(problem)
          # problem = convertproblem(problem)
           #problem = [int(x) for x in problem]
           if action == "*":
               problemanswer = math.prod(problem)
           elif action == "+":
               problemanswer = sum(problem)
           print("addin to total: " + str(problemanswer))
           problemanswertotal = problemanswertotal + problemanswer
       print("Total is " + str(problemanswertotal))











if __name__ == '__main__':
    main()
