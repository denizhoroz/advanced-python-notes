import argparse

parser = argparse.ArgumentParser(description="Example of using argparse")

parser.add_argument('--name', type=str, required=True, help='Your name')
parser.add_argument('--age', type=int, required=True, help='Your age')

args = parser.parse_args()

print(f"Hello, {args.name}! You are {args.age} years old.")

# To run this script, save it as argparser.py and execute it from the command line:
# python argparser.py --name Alice --age 30