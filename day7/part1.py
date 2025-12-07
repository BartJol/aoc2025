import math

def main():
    with open("input.txt", mode="r") as inputfile:
   # with open("example.txt", mode="r") as inputfile:
       splitter_array = []
       for line in inputfile:
           line = line.rstrip("\n")
           splitter_array.append([ch for ch in line])
       firstline = splitter_array[0]
       splitter_array.pop(0)
       initial_tac_man = []
       for position in range(0,len(firstline)):
           if firstline[position] == "S":
               initial_tac_man.append(position)
       print("Initial positions are:")
       print(initial_tac_man)
       tac_man_pos = initial_tac_man
       split_count = 0
       for line in splitter_array:
           #print((''.join(line)))
           new_tac_man_pos = []
           for beam in tac_man_pos:
               if line[beam] == "^":
                   new_tac_man_pos.append(int(beam) - 1)
                   new_tac_man_pos.append(int(beam) + 1)
                   split_count = split_count + 1
                #   print("Beam has been splitted on position " + str(beam))
               else:
                   new_tac_man_pos.append(beam)
           tac_man_pos = set(new_tac_man_pos)
       print("The tac manifolt beam has been splitted " + str(split_count) + " times")








if __name__ == '__main__':
    main()
