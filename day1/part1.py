

def main():
  #  with open("input.txt", mode="r") as inputfile:
    with open("example.txt", mode="r") as inputfile:

        for line in inputfile:
            instructions.append(line.rstrip())
 #       print(len(instructions))
#        print(instructions)
        start = 50
#        positions = range(100)
        zerocount = 0
        for instruction in instructions:
            amount = int(instruction[1:])
            if amount > 100:
                stramount = str(amount)[1:]
                amount = int(stramount)

            direction = instruction[:1]
      #      print("Go " + direction +" " + amount + " steps")
            if direction == "L":
                adjusted_amount = start - int(amount)
            else:
                adjusted_amount = start  + int(amount)

            if adjusted_amount > 99:
                start = adjusted_amount - 100
            elif adjusted_amount < 0:
                start = adjusted_amount + 100
            else:
                start = adjusted_amount
            if start == 0:
                zerocount = zerocount + 1
                print("found zero at direction " + direction + " and amount " + str(amount))


        print("amount on zero is " + str(zerocount))

if __name__ == '__main__':
    main()
