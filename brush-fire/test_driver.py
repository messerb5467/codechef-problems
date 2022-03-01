#!/usr/bin/env python3
import argparse
from test import Test

def process_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file',
                        help='A test file containing graph data to run burn simulations on.')
    args = parser.parse_args()
    return args.test_file

def main():
  test_file = process_parameters()
  with open(test_file) as f:
    num_tests = int(f.readline().strip())
    for _ in range(num_tests):
        tester = Test(f)
        tester.run_burn_simulation()

if __name__ == '__main__':
    main()