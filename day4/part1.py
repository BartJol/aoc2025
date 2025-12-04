

def main():
    with open("input.txt", mode="r") as inputfile:
  #  with open("example.txt", mode="r") as inputfile:
        moveablepaper = 0
        flourplan = []
        for line in inputfile:
            linearray = ['w']
            linearray += list(str(line.rstrip()))
            linearray.append('w')
            flourplan.append(linearray)
        linelength = len(flourplan[0])

        wallline = ['w'] * linelength
        flourplan.append(wallline)
        flourplan.insert(0,wallline)
      #  for line in flourplan:
 #          print(line)
        #print(linelength)
        numberoflines = len(flourplan)
        for row in range(1,numberoflines-1):
            print(flourplan[row])
            rowplussrroundingrows = [flourplan[row-1],flourplan[row],flourplan[row+1]]
            moveablepaperinrow = getmoveablepaperinrow(rowplussrroundingrows,linelength)
            moveablepaper = moveablepaper + moveablepaperinrow
        print("Total number of free rolls is " + str(moveablepaper))



def getmoveablepaperinrow(rowplussrroundingrows,linelenght):
    freerolls = 0
    for position in range(1,linelenght-1):
        if rowplussrroundingrows[1][position] == '@':
            rowbeforesection = rowplussrroundingrows[0][position-1:position+2]
            rowaftersection = rowplussrroundingrows[2][position-1:position+2]
            currentrowsection = [rowplussrroundingrows[1][position-1], rowplussrroundingrows[1][position+1 ]]
            allsurroundingobjcts = rowbeforesection + rowaftersection + currentrowsection
            print(allsurroundingobjcts)
            if len(allsurroundingobjcts) != 8:
                print("incorrect number surrounding objects")
            surroundingrolls = allsurroundingobjcts.count('@')
            if surroundingrolls < 4:
                freerolls = freerolls + 1
    print("Number of freerolls in this line is " + str(freerolls))
    return freerolls






if __name__ == '__main__':
    main()
