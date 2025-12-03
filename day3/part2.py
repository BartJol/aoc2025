

def main():
    with open("input.txt", mode="r") as inputfile:
  #  with open("example.txt", mode="r") as inputfile:
        numbertotal = 0
        for line in inputfile:
            numberlist = []
            banks = list(str(line.rstrip()))
            banksstartlocation = 0
            banksendlocation = len(banks) - 11

            while len(numberlist) < 12:
                array = banks[banksstartlocation:banksendlocation]
                highestnumber, highestposition = higehestnumberandposition(array)
                numberlist.append(highestnumber)
                banksstartlocation = banksstartlocation + highestposition + 1
                banksendlocation = banksendlocation + 1
            completehighnumer = ''.join(numberlist)
            numbertotal = numbertotal + int(completehighnumer)
            print("Number found is " + str(completehighnumer))



        print("Total is " + str(numbertotal))


def higehestnumberandposition(array):
    uniquesortedarray = sorted(set(array))
    highestnumber = uniquesortedarray[-1]
    highestposition = array.index(highestnumber)
    return(highestnumber,highestposition)

if __name__ == '__main__':
    main()
