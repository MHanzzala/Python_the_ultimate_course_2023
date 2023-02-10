import argparse


my_parser = argparse.ArgumentParser(prog="app")

my_parser.add_argument('arg1', help='dummuy arg 1')
my_parser.add_argument('arg2', help='dummuy arg 2')

args = my_parser.parse_args()
print("done executing")