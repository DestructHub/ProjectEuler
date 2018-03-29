#!/usr/bin/env python
# coding=utf-8
def nim():
    binary_map = [0,1]
    total = 3
    for k in range(28):
        binary_map_new = []
        for i in range(0, len(binary_map), 2):
            if binary_map[i:i+2] == [0,0]:
                binary_map_new.extend([0,0,0,1])
                total += 3
            elif binary_map[i:i+2] == [0,1]:
                binary_map_new.extend([0,0])
                total += 2

        binary_map = binary_map_new
        
    return total

if __name__ == "__main__":
    print(nim())
