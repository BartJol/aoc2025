import math

import numpy as np


def main():
   # with open("input.txt", mode="r") as inputfile:
    with open("example.txt", mode="r") as inputfile:
       boxes = []
       for line in inputfile:
           line = line.rstrip("\n")
           stringline = line.split(",")
           int_line = [int(coordinate) for coordinate in stringline]
           boxes.append(int_line)
       box_distances = []
       print(boxes[0])
       print(len(boxes))
       for boxnr in range(0,len(boxes)):
           single_box_distances = np.array([], dtype=float)
           if boxnr != len(boxes) - 1:
               for other_box in range(boxnr+1,len(boxes)):
                   distance = math.dist(boxes[boxnr], boxes[other_box])
                   #print(type(distance) )
                   single_box_distances = np.append(single_box_distances, distance)
                   #print(single_box_distances)
               box_distances.append(single_box_distances)

       for boxnr in range(0,len(box_distances)):
           print(box_distances[boxnr])
       box_instances_indexes = []
       for boxnr in range(0,len(box_distances)):
           sorted_indices = np.argsort(box_distances[boxnr])
           box_instances_indexes.append(sorted_indices)
       #for boxnr in range(0,len(box_instances_indexes)):
       #    print(box_instances_indexes[boxnr])

       connected_boxes = 0
       connections per box = [0] * len(boxes)
       while connected_boxes < 10:
           for box in len(box_distances):
               shortest_connection_per_box_for_all_boxes = []
               shortest_connection_for_box = box.index(connected_boxes[box])

               shortest_connection_per_box_for_all_boxes.append(box_distances[box][shortest_connection_for_box])







if __name__ == '__main__':
    main()
