import textwrap

def main():
    with open("input.txt", mode="r") as inputfile:
  #  with open("example.txt", mode="r") as inputfile:

        for line in inputfile:
            idranges = line.rstrip().split(",")
#        print(idranges)
        totalinvalidid = 0
        for range in idranges:
            start = range.split("-")[0]
            end = range.split("-")[1]
            print("range starts at " + start + " and ends with " + end)

            number = start
            while int(number) <= int(end):
 #               firsthalf, secondhalf = number[:len(number) // 2], number[len(number) // 2:]
  #              if firsthalf == secondhalf:
  #                 totalinvalidid = totalinvalidid + int(number)
  #                  print("Adding " + number + " to total, new total is: " + str(totalinvalidid))
                length = len(number)
                halflength = length // 2
                position = 1
                while position >= 1 and position <= halflength:
                    firstpart = number[:position]
  #                  print(firstpart)
                    position = position + 1
                    if len(number) % len(firstpart) == 0:
                        numberofparts = len(number) / len(firstpart)
    #                    print("There are " + str(numberofparts) + " parts")
                        arrayofnumberparts = textwrap.wrap(number, len(firstpart))
   #                     print((arrayofnumberparts))
                        uniqueelements = set(arrayofnumberparts)

                        if len(uniqueelements) == 1:
                            totalinvalidid = totalinvalidid + int(number)
                            print("Number " + number + " will be added to the total. New total is: " + str(totalinvalidid))
                            break




                number = str(int(number) + 1)
        print("total of invalid ranges is " + str(totalinvalidid))

if __name__ == '__main__':
    main()
