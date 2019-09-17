import argparse
parser = argparse.ArgumentParser(description="Addnumbers")
parser.add_argument("first", type=int)
parser.add_argument("second", type=int)
args = parser.parse_args()
a = args.first
b = args.second
c = a + b
print("adition of {} and {} = {}".format(a, b, c))

