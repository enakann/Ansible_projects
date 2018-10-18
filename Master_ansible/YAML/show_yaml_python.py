import sys

file1=sys.argv[1]
print(file1)
import yaml
import pprint
pprint.pprint(yaml.load(open(file1).read()))
