import sys

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s*3 # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

def main():
    # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:
      name = sys.argv[1]
    else:
      name = 'World'
    if name == 'Guido':
        print(repeat(name,1) + '!!!')
    else:
        print(repeat(name,1))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
