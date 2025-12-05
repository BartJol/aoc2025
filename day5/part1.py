

def main():
    with open("input.txt", mode="r") as inputfile:
  #  with open("example.txt", mode="r") as inputfile:
        inputtype = "freshrange"
        freshrangearray = []
        productids = []
        freshproducts = []
        for line in inputfile:
            lineinput = line.rstrip()

            if lineinput == "":
                inputtype = "ids"
                #next()
            elif inputtype == "freshrange":
                range = lineinput.split("-")
                freshrangearray.append(range)
            elif inputtype == "ids":
                productids.append(lineinput)
        #print(freshrangearray)
        #print(productids)
        for productid in productids:
            for range in freshrangearray:
                if int(productid) < int(range[0]) or int(productid) > int(range[1]):
                    continue
                else:
                    print("Product id " + str(productid) + " is fresh")
                    print("This fals in range " + str(range[0]) + "-" + str(range[1]))
                    freshproducts.append(productid)
                    break
        print(freshproducts)
        print("there are " + str(len(freshproducts)) + " Fresh products")







if __name__ == '__main__':
    main()
