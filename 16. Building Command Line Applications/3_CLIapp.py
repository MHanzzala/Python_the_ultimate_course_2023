import argparse


my_parser = argparse.ArgumentParser(
    prog="app", description='Returns the Addition, multiplication, division and subtraction of any two numbers')

my_parser.add_argument('arg1', help='The First Entry', type=int)
my_parser.add_argument('arg2', help='The Second Entry', type=int)

args = my_parser.parse_args()

input1 = args.arg1
input2 = args.arg2

print("The Summation is:", input1+input2)
print("The Subtraction is:", input1-input2)
print("The Multiplication is:", input1*input2)
print("The Division is:", input1/input2)
print("done executing")
