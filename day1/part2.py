

def main():
  #  with open("input.txt", mode="r") as inputfile:
    with open("example.txt", mode="r") as inputfile:
        instructions = []
        for line in inputfile:
            instructions.append(line.rstrip())
 #       print(len(instructions))
#        print(instructions)
        start = 50
#        positions = range(100)
        zeroclickcount = 0
        number = 0
        for instruction in instructions:
            number = number +1
            amount = int(instruction[1:])
            if amount >= 1000:
                break
            if amount >= 100:
                stramount = str(amount)[1:]
                numberofrounds = int(str(amount)[:1])
                amount = int(stramount)

                zeroclickcount = zeroclickcount + numberofrounds
                print("adding " + str(numberofrounds) + " to total")

            direction = instruction[:1]
      #      print("Go " + direction +" " + amount + " steps")
            if direction == "L":
                adjusted_amount = start - int(amount)
            else:
                adjusted_amount = start  + int(amount)
            print("Start: " + str(start) + " and amount " + str(amount) + " direction " + direction + " and  zeroes " + str(zeroclickcount))
            if adjusted_amount > 99:
                start = adjusted_amount - 100
                zeroclickcount = zeroclickcount + 1
                print("going above 99 " + direction + " and amount " + str(amount))
            elif adjusted_amount < 0:

                if start > 0:
                    zeroclickcount = zeroclickcount + 1
                    print("going below 0 " + direction + " and amount " + str(amount))
                start = adjusted_amount + 100
            else:
                start = adjusted_amount
            if start == 0 and adjusted_amount != 100:
                zeroclickcount = zeroclickcount + 1
                print("found zero at direction " + direction + " and amount " + str(amount))
            if start < 0 or start > 99:
                print(str(start) + " on line " + str(number) )
                break


        print("amount on zero is " + str(zeroclickcount))

if __name__ == '__main__':
    main()
