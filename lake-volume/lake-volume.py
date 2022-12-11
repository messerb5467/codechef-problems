#!/usr/bin/env python3
import argparse
import numpy as np
class Island:
    def __init__(self,
                 elev_data_file):
        self.elev_data = np.loadtxt(elev_data_file)
        self.total_lake_volume = 0
        self.curr_lake_volume = 0
        self.curr_lake_height = 0
        self.found_lake = False
        self.forward_volumes = []
        self.backward_volumes = []

    def find_total_lake_volume(self):
        left_index, right_index = 0, len(self.elev_data) - 1
        left_max, right_max = 0, 0
        lake_volume = 0
        while left_index < right_index:
            if self.elev_data[left_index] < self.elev_data[right_index]:
                left_max = max(left_max, self.elev_data[left_index])
                lake_volume += max(0, left_max - self.elev_data[left_index])
                left_index += 1
            else:
                right_max = max(right_max, self.elev_data[right_index])
                lake_volume += max(0, right_max - self.elev_data[right_index])
                right_index -= 1
        print(lake_volume)

def process_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('elev_data_file',
                        help='The elevation data we want to run simulations with.')
    return parser.parse_args()

def main():
    args = process_parameters()
    island = Island(args.elev_data_file)
    island.find_total_lake_volume()

if __name__ == '__main__':
    main()
