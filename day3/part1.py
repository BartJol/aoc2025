

def main():
    with open("input.txt", mode="r") as inputfile:
  #  with open("example.txt", mode="r") as inputfile:
        numbertotal = 0
        for line in inputfile:
            banks = list(str(line.rstrip()))
            uniquebanks = sorted(set(banks))
            highestnumber = uniquebanks[-1]
            highestnumberlocation = banks.index(highestnumber)
            print("highest number is " + highestnumber + " on location " + str(highestnumberlocation))
            print(len(banks))
            if highestnumberlocation == len(banks) -1:
                secondnumber = highestnumber
                firstnumber = uniquebanks[-2]
            else:
                firstnumber = highestnumber
                restofarray = banks[(highestnumberlocation + 1):]
                restunique = sorted(set(restofarray))
                secondnumber = restunique[-1]
            numberstring = firstnumber + secondnumber
            print("Adding " + numberstring + " to total")
            numbertotal = numbertotal + int(numberstring)
        print("Total is " + str(numbertotal))


if __name__ == '__main__':
    main()
