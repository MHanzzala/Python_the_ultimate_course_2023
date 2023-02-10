import argparse


my_parser = argparse.ArgumentParser(prog="app", description='Returns the Addition, multiplication, division and subtraction of any two numbers')

my_parser.add_argument('arg1', help='The First Entry', type=int)
my_parser.add_argument('arg2', help='The Second Entry', type=int)
my_parser.add_argument('--arg3', help='Shift Optional arg', type=int)
my_parser.add_argument('--arg4', help='Shift Optional arg', action='store_true')
args = my_parser.parse_args()

input1 = args.arg1
input2 = args.arg2
input3 = args.arg3
input4 = args.arg4

if input3 ==None:
    shift =5
else:
    shift = input3
    
print("The Summation is:", input1+input2+shift)
print("The Subtraction is:", input1-input2+shift)
print("The Multiplication is:", input1*input2+shift)
print("The Division is:", input1/input2+shift)
if input4 ==True:
    print("The power of 2 of the first arg", input1*input1)

print("done executing")