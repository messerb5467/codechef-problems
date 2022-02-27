import argparse
from test import Test

def process_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file',
                        help='A test file containing graph data to run burn simulations on.')
    return parser.parse_args()

def main():
  test_file = process_parameters()
  with open(test_file) as f:
    num_tests = int(f.readline())
    for _ in range(num_tests):
        tester = Test(f)
        tester.run_burn_simulation()