import argparse
parser=argparse.ArgumentParser(description="Choices")
parser.add_argument("sub", choices=['physics', 'math', 'biology'])
args=parser.parse_args()
print("My subject is ", args.sub)
