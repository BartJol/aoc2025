

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
            if not len(start) % 2 == 0 and len(start) == len(end):
                print("This range only has odd amount of length")
            else:
                number = start
                while int(number) <= int(end):
                    firsthalf, secondhalf = number[:len(number) // 2], number[len(number) // 2:]

                    if firsthalf == secondhalf:
                        totalinvalidid = totalinvalidid + int(number)
                        print("Adding " + number + " to total, new total is: " + str(totalinvalidid))
                    number = str(int(number) + 1)
        print("total of invalid ranges is " + str(totalinvalidid))

if __name__ == '__main__':
    main()
