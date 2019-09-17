import argparse
parser = argparse.ArgumentParser(description="Optional Argument")
parser.add_argument("name")
parser.add_argument("--suname")
args = parser.parse_args();
print("Name is", args.name, end=' ')
if args.suname:
    print(args.suname)

