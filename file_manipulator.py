import sys

commands = {
    'reverse' : 4,
    'copy' : 4,
    'duplicate-contents' : 4,
    'replace-string' : 5
}

def validate_args(args):
    if len(args) <= 3 or len(args) >= 6:
        return False
    
    command = args[1]
    
    if command not in commands or commands[command] != len(args):
        return False
    
    return True

def reverse(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    reversed_contents = contents[::-1]
    with open(outputpath, 'w') as f:
        f.write(reversed_contents)

def copy(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)

def duplicate_contents(inputpath, n):
    with open(inputpath) as f:
        contents = f.read()
    duplicated_contents = contents
    for _ in range(n):
        with open(inputpath, 'a') as f:
            f.write(duplicated_contents)

def replace_string(inputpath, needle, newstring):
    with open(inputpath) as f:
        contents = f.read()    
    replaced_contents = contents.replace(needle, newstring)
    with open(inputpath, 'w') as f:
        f.write(replaced_contents)

def main():
    args = sys.argv

    if not validate_args(args):
        print('Error: Please enter the correct input!\nFor more information, see the README.md')
        return

    if args[1] == 'reverse':
        reverse(args[2], args[3])
    elif args[1] == 'copy':
        copy(args[2], args[3])
    elif args[1] == 'duplicate-contents':
        duplicate_contents(args[2], int(args[3]))
    elif args[1] == 'replace-string':
        replace_string(args[2], args[3], args[4])

if __name__ == "__main__":
    main()