import sys

# sys.argv[0] is ALWAYS the module name (file name)
# every following system argument variable is a string

for _ in sys.argv:
    print(f'The system received an argument: {_}')